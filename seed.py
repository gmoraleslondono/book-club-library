import sqlite3

DB_PATH = "library.db"

authors = [
    (1, "Terry", "Pratchett"),
    (2, "Neil", "Gaiman"),
    (3, "Ursula", "Le Guin"),
    (4, "Frank", "Herbert"),
    (5, "Astrid", "Lindgren"),
    (6, "William", "Gibson"),
    (7, "Frederik", "Pohl"),
]

books = [
    (1, "Good Omens", 1990, "Fantasy"),
    (2, "Dune", 1965, "Sci-Fi"),
    (3, "A Wizard of Earthsea", 1968, "Fantasy"),
    (4, "Pippi Longstocking", 1945, "Children"),
    (5, "The Colour of Magic", 1983, "Fantasy"),
    (6, "American Gods", 2001, "Fantasy"),
    (7, "Neuromancer", 1984, "Sci-Fi"),
    (8, "Gateway", 1977, "Sci-Fi"),
]

book_authors = [
    (1, 1),  # Good Omens, Terry Pratchett
    (1, 2),  # Good Omens, Neil Gaiman
    (2, 4),  # Dune, Frank Herbert
    (3, 3),  # A Wizard of Earthsea, Ursula Le Guin
    (4, 5),  # Pippi Longstocking, Astrid Lindgren
    (5, 1),  # The Colour of Magic, Terry Pratchett
    (6, 2),  # American Gods, Neil Gaiman
    (7, 6),  # Neuromancer, William Gibson
    (8, 7),  # Gateway, Frederik Pohl
]

members = [
    (1, "Emily", "Carter", "emily.carter@example.com"),
    (2, "James", "Whitaker", "james.whitaker@example.com"),
    (3, "Olivia", "Bennett", "olivia.bennett@example.com"),
    (4, "Daniel", "Foster", "daniel.foster@example.com"),
    (5, "Hannah", "Brooks", "hannah.brooks@example.com"),
    (6, "Thomas", "Reid", "thomas.reid@example.com"),
]

loans = [
    (1, 1, 2, "2026-09-01", "2026-09-15", "2026-09-12"),  # Dune, returned
    (2, 2, 2, "2026-09-20", "2026-10-04", "2026-10-02"),  # Dune again, returned
    (3, 1, 1, "2026-10-10", "2026-10-24", None),          # Good Omens, OVERDUE
    (4, 3, 3, "2026-10-20", "2026-11-03", None),          # Earthsea, open, not overdue
    (5, 2, 6, "2026-09-05", "2026-09-19", "2026-09-18"),  # American Gods, returned
    (6, 4, 7, "2026-10-12", "2026-10-26", "2026-10-20"),  # Neuromancer, returned
]


def insert_values():
    """Insert test data into library.db. The tables must exist beforehand."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    # Insert Authors
    conn.executemany("INSERT INTO authors (author_id, first_name, last_name) VALUES (?, ?, ?)", authors)

    # Insert Books
    conn.executemany("INSERT INTO books (book_id, title, year, genre) VALUES (?, ?, ?, ?)", books)

    # Insert Book Authors
    conn.executemany("INSERT INTO book_authors (book_id, author_id) VALUES (?, ?)", book_authors)

    # Insert Members
    conn.executemany("INSERT INTO members (member_id, first_name, last_name, email) VALUES (?, ?, ?, ?)", members)

    # Insert Loans
    conn.executemany("INSERT INTO loans (loan_id, member_id, book_id, loan_date, due_date, return_date) VALUES (?, ?, ?, ?, ?, ?)", loans)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_values()