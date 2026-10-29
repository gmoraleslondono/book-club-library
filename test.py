import requests

response = requests.get("https://openlibrary.org/search.json?q=shrooms")

print(response.json())

books = []
for items in response["docs"]:
    authors = ",".join(book.get("author_name", ["Unknown Author"]))
    year = book.get("first_publish_year")

    books.append((book_id, ))