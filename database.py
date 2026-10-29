import sqlite3

from seed import insert_values

DB_PATH = "library.db"

def get_books_in_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("select * from books")
    return cursor.fetchall()

def add_book(book):

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    books = get_books_in_db()
    new_id = len(books) + 1
    conn.execute("INSERT INTO books (book_id, title, year) VALUES (?, ?, ?)", 
                         (new_id, book["title"], book["year"]))
    conn.commit()
    conn.close()


"""
def add_author(author_data):

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    if len(author_data) > 1:
            for ad in author_data:
                conn.execute("INSERT INTO book_authors (book_id, title, year, genre) VALUES (?, ?, ?, ?)", 
                                         (new_id, ad))
    conn.execute("INSERT INTO book_authors (book_id, title, year, genre) VALUES (?, ?, ?, ?)", 
                                             (new_id, author_data))
    
    conn.commit()
    conn.close()
"""
def update_database():
    add_book()
    add_author()
    add_book_authors()

def _get_connection():
    """Open a connection to the database with foreign keys enabled."""

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def _rebuild_tables():
    """Drop and recreate all tables by running schema.sql."""

    # Connect to database
    conn = _get_connection()

    try:
        # Reads schema.sql to create tables.
        with open("schema.sql", encoding="utf-8") as file:
            conn.executescript(file.read())

    finally:
        conn.close()

def clear_data():
    """Rebuild the tables from schema.sql, without data."""

    # Rebuilds tables
    _rebuild_tables()

def reset_db():
    """Rebuild the tables from schema.sql and insert the seed data."""

    # Rebuilds tables
    _rebuild_tables()

    # Fill tables with seed data
    insert_values()


def _add_book_author(book_id, author_id):
    """Link a book to an author, if they aren't linked already."""

    # Checks if ids are null
    if book_id is None or author_id is None:
        raise ValueError("book_id and author_id are required")

    # Connect to database
    conn = _get_connection()

    try:
        cursor = conn.cursor()

        # Adds book_author to database
        cursor.execute("INSERT OR IGNORE INTO book_authors (book_id, author_id) VALUES (?, ?)", (book_id, author_id))

        conn.commit()
    finally:
        conn.close()


def _add_author(name):
    """Return the author_id for an author, add them first if they're new."""

    # Connect to database
    conn = _get_connection()

    try:
        cursor = conn.cursor()

        # Checks if author already exists
        cursor.execute("SELECT author_id FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()

        # If author exists
        if row is not None:

            # Return the id of the existing author
            return row[0]

        # Adds author to database
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        conn.commit()

        # Returns the id of the new author
        return cursor.lastrowid
    finally:
        conn.close()


def _add_book(title, year):
    """Return the book_id for a book, add it first if it's new."""

    # Connect to database
    conn = _get_connection()

    try:
        cursor = conn.cursor()

        # Checks if book already exists
        cursor.execute("SELECT book_id FROM books WHERE title = ? AND year = ?", (title, year))
        row = cursor.fetchone()

        # If book exists
        if row is not None:

            # Return the id of the existing book
            return row[0]

        # Adds book to database
        cursor.execute("INSERT INTO books (title, year) VALUES (?, ?)", (title, year))
        conn.commit()

        # Returns the id of the new book
        return cursor.lastrowid
    finally:
        conn.close()


def update_db(title: str, year: int, author_names: list[str] | None = None):
    """Add a book, with its authors, skipping anything that already exists."""

    book_id = _add_book(title, year)

    # If the book has authors
    if author_names is not None:
        for name in author_names:
            author_id = _add_author(name)
            _add_book_author(book_id, author_id)