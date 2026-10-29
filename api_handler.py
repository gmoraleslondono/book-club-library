import requests

url = "https://openlibrary.org/search.json"

class ApiHandler():
    def pretty_print(self, books):

        print(f"{"Title":<65} {"Author(s)":<60} {"Published Year":<5}")
        for book in books["docs"]:
            authors = ",".join(book.get("author_name", "Unknown Author"))
            year = book.get("first_publish_year", "N/A")

            print(f"{book['title']:<65} {authors:<60} {year:<5}")

    def get_books(self):  
        headers = {"User-Agent": "OpenLibraryStudentProject"}
        search_parameters = {"q" : "sci-fi", "limit" : 15} # here we put input() later on
        
        open_library_books = requests.get(url, headers=headers, params=search_parameters).json()
        self.pretty_print(open_library_books)

    def display_books_per_category(self):
        print("\nHi! Welcome to our fantastic online library. Please type your search keyword(s) to display top 10 available books:")
        try:
            search_string = input().lower()
            headers = {"User-Agent": "OpenLibraryStudentProject"}
            search_parameters = {"q" : search_string, "limit" : 10} 
            open_library_books = requests.get(url, headers=headers, params=search_parameters).json()
            
            print("\n\nDATA GENERATED FROM API\n\n")
            self.pretty_print(open_library_books)

            # break or next input to select one of the available books

        except RuntimeError, TypeError, NameError, ValueError:
            pass
