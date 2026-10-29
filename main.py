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
    print("Welcome to our library. Please take a look at our local library and see if you wish to loan any of the books.\n")
    pretty_print(available_books)
    print("\nIf you wish to book any of the dispalyed book, please type the desired ID. If you wish to browse yourself, please type the word 'next'\n")
    while True:
        choice = input()
        # add a method to select one of the generated books

        # Proceed to the API call if the user does NOT want any of the pre-generated books.
        api_obj = ApiHandler()
        api_obj.display_books_per_category()
        #*args