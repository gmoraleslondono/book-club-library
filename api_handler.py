import requests
from input_handler import select_book_from_api

url = "https://openlibrary.org/search.json"

class ApiHandler():
    def pretty_print(self, books):

        print(f"{"ID":<3} {"Title":<65} {"Author(s)":<60} {"Published Year":<5}")
        clean_book_list = []
        book_id = 1
        for book in books["docs"]:
            authors = ", ".join(book.get("author_name", ["Unknown Author"]))
            year = book.get("first_publish_year")

            clean_book_list.append((book_id, book["title"], year))
            
            print(f"{book_id:<3} {book['title']:<65} {authors:<60} {year:<5}")
            book_id += 1
        return clean_book_list

    def get_books(self):  
        headers = {"User-Agent": "OpenLibraryStudentProject"}
        search_parameters = {"q" : "sci-fi", "limit" : 15} # here we put input() later on
        
        open_library_books = requests.get(url, headers=headers, params=search_parameters).json()
        self.pretty_print(open_library_books)



    def display_books_per_category(self):
        print("\nHi! Welcome to our fantastic online library. Please type your search keyword(s) to display top 10 available books:\n")
        try:
            search_string = input().lower()
            headers = {"User-Agent": "OpenLibraryStudentProject"}
            search_parameters = {"q" : search_string, "limit" : 10} 
            open_library_books = requests.get(url, headers=headers, params=search_parameters).json()
            
            print("\nDATA GENERATED FROM API\n")
            clean_book_list = self.pretty_print(open_library_books)

            select_book_from_api(clean_book_list)

        except RuntimeError, TypeError, NameError, ValueError:
            pass
