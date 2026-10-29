import sys
from database import update_db, get_books_in_db

def get_book(clean_book_list, user_input):
    for id, title, authors, year in clean_book_list:
        if id == user_input:
            return {"title" : title, "year" : year, "authors" : authors}
    return None

def select_book_from_api(clean_book_list):
    print("\nWould you like to book any of the displayed books? If yes, please specify ID, if not, please type 'N'\n")
    user_input = input().strip()
    
    if user_input.isdigit():

        loaned_book = get_book(clean_book_list, int(user_input))
        if loaned_book is None:
            print("No book with that ID.")
            return

        # refine to use as args
        if loaned_book["year"] == "N/A":
            update_db(loaned_book["title"], author_names = loaned_book["authors"])
        else:
            update_db(loaned_book["title"], loaned_book["year"], loaned_book["authors"])

        print("\nHere, we should get our loaned book added to DB.")
        for row in get_books_in_db():
            print(row)
        # added data to the loans db; 

    else:
        print("For now, no book.")
        return