from dao.book_repository import BookRepository
from entity.book import Book


class BookService:
    def __init__(self, book_repo: BookRepository):
        self._book_repo = book_repo

    def add_book(self, book: Book):
        # TODO validation
        self._book_repo.create(book)
        self._book_repo.save()

    def get_all_books(self):
        return self._book_repo.find_all()

    def get_all_book_by_id(self, id):
        return self._book_repo.find_by_id(id)

    def reload_books(self):
        self._book_repo.load()
        print(self.get_all_books())

    def save_books(self):
        self._book_repo.save()
        print("Books saved successfully.")