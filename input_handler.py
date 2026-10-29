import sys
from database import add_book, get_books_in_db

def get_book(clean_book_list, user_input):
    for id, title, authors, year in clean_book_list:
        if id == user_input:
            return {"title" : title, "year" : year}
    return None

def select_book_from_api(clean_book_list):
    print("\nWould you like to book any of the displayed books? If yes, please specify ID, if not, please type 'N'\n")
    user_input = input().strip()
    
    if user_input.isdigit():
        loaned_book = get_book(clean_book_list, int(user_input))
        if loaned_book is None:
            print("No book with that ID.")
            return
        
        add_book(loaned_book)
        print("\nHere, we should get our loaned book added to DB.")
        for row in get_books_in_db():
            print(row)

        sys.exit()
    elif "N":
        print("For now, no book.")
    else:
        print("For now, wrong input.")