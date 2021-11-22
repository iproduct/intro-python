import json

from book import Book
from book_repository import BookRepository

DEFAULT_BOOKS_DB_FILE = "books.json"

class BookRepositoryJson(BookRepository):
    def __init__(self, filename=DEFAULT_BOOKS_DB_FILE):
        super().__init__()
        self.db_file_name = filename

    def load(self):
        books_list = load_from_file(self.db_file_name)
        for b in books_list:
            book = Book(b["title"], b["subtitle"], b["authors"],
                    b["isbn"], b["publisher"], b["year"], b["price"], b["genre"], b["tags"], b["description"])
            book.id = b["id"]
            self.insert(book)

    def persist(self):
        save_to_file(self.db_file_name, self.books)


# helpers
def save_to_file(filename, books):
    """Save books data to JSON file"""
    with open(filename, "wt") as f:
        json.dump(books, f, indent=4)

def load_from_file(filename):
    """Load books data from JSON file"""
    with open(filename, "rt") as f:
        return json.load(f)
