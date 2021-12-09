from tkinter import *
from tkinter import messagebox

from dao.book_repository_json import BookRepositoryJson
from model.book import Book
from presentation.add_edit_book_dialog import AddEditBookDialog
from presentation.app_main_window import AppMainWindow
from presentation.show_items_view import ShowItemsView
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

    def browseBooks(self):
        self.book_repository.load()
        books = self.book_repository.find_all()
        self.show_books_view = ShowItemsView(self.root, items=books, item_class=Book,
             add_command=self.show_add_book, edit_command=self.show_edit_book, delete_command=self.delete_books, )

    def show_add_book(self):
        self.add_book_dialog = AddEditBookDialog(self.root, application=self)

    def show_edit_book(self, books):
        if len(books) == 0:
            messagebox.showinfo(title="Edit Book Dialog", message="Please select a book to edit.")
            return
        edited_book = self.book_repository.find_by_id(books[0][0])
        self.add_book_dialog = AddEditBookDialog(self.root, book=edited_book, application=self)

    def add_edit_book(self, book):
        if book.id:
            self.book_repository.update(book) #edit existing book
        else:
            self.book_repository.insert(book) # add new book
        self.book_repository.persist()
        self.show_books_view.set_items(self.book_repository.find_all())

    def delete_books(self, books):
        for book_tuple in books:
            self.book_repository.delete_by_id(book_tuple[0])
        self.book_repository.persist()
        self.show_books_view.set_items(self.book_repository.find_all())


if __name__ == '__main__':
    app = Application(BookRepositoryJson(id_sequence=uuid_sequence_generator()))
    app.start()
