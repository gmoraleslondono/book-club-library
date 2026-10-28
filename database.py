import sqlite3

from seed import insert_values

DB_PATH = "library.db"


def _rebuild_tables():
    """Drop all tables by running schema.sql"""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    # Reads schema.sql to create tables. Closes when done
    with open("schema.sql") as file:
        conn.executescript(file.read())

    conn.close()