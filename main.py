from database import reset_db, get_books_in_db
from api_handler import ApiHandler
import sys

def main_pretty_print(books):
    print(f"{"ID":<3} {"Title":<25} {"Published Year":<5}")
    for book in books:
        print(f"{book[0]:<3} {book[1]:<25} {book[2]:<5}")

if __name__ == "__main__":
    
    reset_db()
    available_books = get_books_in_db()
    print("Welcome to our library. Please take a look at our local library and see if you wish to loan any of the books.\n")
    main_pretty_print(available_books)
    print("\nIf you wish to book any of the displayed books, please type the desired ID. If you wish to browse yourself, please type the word 'next'\n")
    while True:
        choice = input().lower()
        # add a method to select one of the generated books
        if choice == "next":
            api_obj = ApiHandler()
            api_obj.display_books_per_category()
        elif choice == "quit":
            sys.exit()
        else:
            # invoke input_handler.py and create function there
            # Gloria, this is here for you to begin with.
            print("\nselect book for id in book['book_id']")
            break