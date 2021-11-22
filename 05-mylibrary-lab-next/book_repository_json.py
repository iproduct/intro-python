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
            book = Book(b["id"], b["title"], b["subtitle"], b["authors"],
                        b["isbn"], b["publisher"], b["year"], b["price"], b["genre"], b["tags"], b["description"])
            self.insert(book)

    def persist(self):
        save_to_file(self.db_file_name, self.find_all())


# helpers

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

def obj_hook(clazz):
    def obj_hook(dict):
        obj = clazz()
        obj.__dict__ = dict
        return obj
    return obj_hook


def save_to_file(filename, books):
    """Save books data to JSON file"""
    with open(filename, "wt") as f:
        json.dump(books, f, indent=4, default=dumper)


def load_from_file(filename, entity_class):
    """Load books data from JSON file"""
    with open(filename, "rt") as f:
        return json.load(f, object_hook=obj_hook(entity_class))
