import sqlite3

from seed import insert_values

DB_PATH = "library.db"

def get_books_in_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("select * from books")
    return cursor.fetchall()

def add_book():

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    books = get_books_in_db()
    new_id = len(books) + 1
    conn.execute("INSERT INTO books (book_id, title, year, genre) VALUES (?, ?, ?, ?)", 
                         (new_id, "Prison Island", 2017, "ABRACADABRA"))
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