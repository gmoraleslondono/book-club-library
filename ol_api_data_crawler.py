import requests
from seed import populate_db, create_db

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
        search_parameters = {"q" : "sci-fi", "limit" : 10} # here we put input() later on
        open_library_books = requests.get(url, headers=headers, params=search_parameters).json()
        self.pretty_print(open_library_books)
        self.populate_schema(open_library_books["docs"])

    def populate_schema(self, book_row_data):
        create_db()
        populate_db(book_row_data) 

if __name__ == "__main__":
    api_obj = ApiHandler()
    api_obj.get_books()