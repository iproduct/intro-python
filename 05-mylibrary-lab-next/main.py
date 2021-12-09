from tkinter import *

from dao.book_repository_json import BookRepositoryJson
from model.book import Book
from presentation.add_book_dialog import AddBookDialog
from presentation.app_main_window import AppMainWindow
from presentation.show_books_view import ShowBooksView
from utils.tkinter_utils import print_hierarchy
from utils.uuid_sequence_generator import uuid_sequence_generator


class Application:
    def __init__(self, book_repository=BookRepositoryJson(id_sequence=uuid_sequence_generator())):
        self.book_repository = book_repository

    def start(self):
        self.book_repository.load()
        self.root = Tk()
        self.main_window = AppMainWindow(self.root, self)
        print_hierarchy(self.root)
        self.root.mainloop()

    def showAddBook(self):
        self.add_book_dialog = AddBookDialog(self.root, application=self)

    def addBook(self, book):
        self.book_repository.insert(book)
        self.book_repository.persist()
        self.show_books_view.refresh(self.book_repository.find_all())

    def browseBooks(self):
        self.book_repository.load()
        books = self.book_repository.find_all()
        self.show_books_view = ShowBooksView(self.root, books, entity_cls=Book)


if __name__ == '__main__':
    app = Application(BookRepositoryJson(id_sequence=uuid_sequence_generator()))
    app.start()
