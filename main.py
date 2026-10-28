from database import reset_db, get_books_in_db
from seed import insert_values
from api_handler import ApiHandler

def pretty_print(books):
    print(f"{"ID":<3} {"Title":<50} {"Published Year":<5} {"Genre":<10}")
    for book in books:
        print(book)

if __name__ == "__main__":
    reset_db()

    available_books = get_books_in_db()
    pretty_print(available_books)
    # add a method to select one of the generated books

    # Proceed to the API call if the user does NOT want any of the pre-generated books.
    api_obj = ApiHandler()
    api_obj.display_books_per_category()
    #*args