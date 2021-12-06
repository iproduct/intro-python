from tkinter import *

from dao.book_repository_json import BookRepositoryJson
from presentation.add_book_dialog import AddBookDialog
from presentation.app_main_window import AppMainWindow
from presentation.show_books_view import ShowBooksView
from utils.tkinter_utils import print_hierarchy


class Application:
    def __init__(self, book_repository = BookRepositoryJson()):
        self.book_repository = book_repository

    def start(self):
        self.book_repository.load()
        self.root = Tk()
        self.main_window = AppMainWindow(self.root, self)
        print_hierarchy(self.root)
        self.root.mainloop()

    def addBook(self):
       AddBookDialog(self.root, application=self, books_repo=self.book_repository) # self.add_book_dialog =

    def browseBooks(self):
        self.show_books_view = ShowBooksView(self.main_window )

if __name__ == '__main__':
    app = Application(BookRepositoryJson())
    app.start()



