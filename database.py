import sqlite3

from seed import insert_values

DB_PATH = "library.db"


def _rebuild_tables():
    """Drop and recreate all tables by running schema.sql."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

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


def add_book_author(book_id, author_id):
    """Add a book_author to the database by linking book_id and author_id."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        cursor = conn.cursor()

        # Adds book_author to database
        cursor.execute("INSERT INTO book_authors (book_id, author_id) VALUES (?, ?)", (book_id, author_id))

        conn.commit()
    finally:
        conn.close()


def add_author(name):
    """Add an author to the database and return the new author_id."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        # Adds author to database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))

        conn.commit()

        # Returns the id of the new author
        return cursor.lastrowid
    finally:
        conn.close()


def add_book(title, year):
    """Return the book_id for a book, add it first if it's new."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    try:
        cursor = conn.cursor()

        # Checks if book already exists
        cursor.execute("SELECT book_id FROM books WHERE title = ? AND year = ?", (title, year))
        row = cursor.fetchone()

        # If book exists
        if row is not None:

            # Return existing book id
            return row[0]

        # Adds book to database
        cursor.execute("INSERT INTO books (title, year) VALUES (?, ?)", (title, year))
        conn.commit()

        # Returns the id of the new book
        return cursor.lastrowid

    finally:
        conn.close()