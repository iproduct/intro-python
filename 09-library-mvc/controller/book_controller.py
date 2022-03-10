from datetime import datetime
from tkinter import *

from entity.book import Book
from service.book_service import BookService
from view.command.books.add_book_command import AddBookCommand
from view.command.books.show_add_book_command import ShowAddBookCommand
from view.components.item_form import ItemForm
from view.utils.tkinter_utils import center_resize_window


class BookController:
    def __init__(self, service: BookService, view=None):
        self.view = view
        self.service = service
        self.show_add_book_command = ShowAddBookCommand(self)
        self.add_book_command = AddBookCommand(self)

    def get_all_books(self):
        return self.service.get_all_books()

    def reload_books(self):
        return self.service.reload_books()

    def save_books(self):
        return self.service.save_books()

    def show_add_book(self):
        form = ItemForm(self.view,
                        Book("", "", "", [], "", "", datetime.now().year, 0.0, "", [], ""),
                        self.add_book_command)

    def add_book(self, book: Book):
        self.service.add_book(book)
        self.view.refresh()

    def show_edit_book(self, book_id):
        window = Toplevel(self.view)
        window.title("Add Book")
        from view.components.item_form import ItemForm
        form = ItemForm(window, self.service.get_all_book_by_id(book_id), self.add_book_command, edit=True)
        form.grid(row=0, column=0, sticky=NSEW)
        center_resize_window(window)
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
