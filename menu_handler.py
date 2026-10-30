def view_book_details(book):
    """View the selected book."""
    # Show this book's title, published year, authors, and whether it is currently on loan.
    pass


def borrow_book(book):
    """Borrow the selected book."""
    # Ask which member is borrowing, then save a new loan with a loan date and a due date.
    pass


def return_book(book):
    """Return the selected book."""
    # Find the open loan for this book and set its return date.
    pass


def edit_book(book):
    """Edit the selected book."""
    # Update this book's title, published year, or linked authors.
    pass


def remove_book(book):
    """Remove the selected book."""
    # Delete this book and its author links when it has no open loan.
    pass


def handle_displayed_book_choice(books, choice):
    """Offer every action available for one book from the local library list."""

    if not choice.isdigit():
        print("\nPlease type a book ID, 'next', or 'quit'.")
        return

    book_id = int(choice)
    selected = None
    for book in books:
        if book[0] == book_id:
            selected = book
            break

    if selected is None:
        print("\nNo book with that ID.")
        return

    # These options are the actions on a book that is already displayed.
    _, title, year = selected
    while True:
        print(f"\nSelected: {title} ({year})")
        print("What would you like to do?\n")
        print("1. View details")
        print("2. Borrow")
        print("3. Return")
        print("4. Edit")
        print("5. Remove")
        print("6. Back")

        action = input().strip()
        if action == "6":
            print("\nType another book ID, 'next' to search, or 'quit'.")
            return

        # Each number calls one placeholder. The sentence is the text under that function's name  (_doc_ attribute).
        if action == "1":
            print(f"\nView details: {view_book_details.__doc__}")
            view_book_details(selected)
        elif action == "2":
            print(f"\nBorrow: {borrow_book.__doc__}")
            borrow_book(selected)
        elif action == "3":
            print(f"\nReturn: {return_book.__doc__}")
            return_book(selected)
        elif action == "4":
            print(f"\nEdit: {edit_book.__doc__}")
            edit_book(selected)
        elif action == "5":
            print(f"\nRemove: {remove_book.__doc__}")
            remove_book(selected)
        else:
            print("\nPlease choose one of the options above.")
