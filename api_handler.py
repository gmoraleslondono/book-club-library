import requests
#from database import populate_db, create_db

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
        
        
        #self.populate_schema(open_library_books["docs"])

    def display_books_per_category(self):
        print("\nHi! Welcome to our fantastic online library. Please select a genre to display available books:")
        try:
            genre = input().lower()
            headers = {"User-Agent": "OpenLibraryStudentProject"}
            search_parameters = {"q" : genre, "limit" : 10} 
            open_library_books = requests.get(url, headers=headers, params=search_parameters).json()
            print("\n\n", type(open_library_books),"\n\n")
            self.pretty_print(open_library_books)

        except RuntimeError, TypeError, NameError, ValueError:
            pass
