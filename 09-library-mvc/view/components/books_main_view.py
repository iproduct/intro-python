from tkinter import *
from tkinter import ttk

from controller.book_controller import BookController
from view.command.books.add_book_command import AddBookCommand
from view.command.books.delete_books_command import DeleteBooksCommand
from view.command.books.edit_book_command import ShowEditBookCommand
from view.command.books.show_add_book_command import ShowAddBookCommand
from view.components.item_list import ItemList
from view.utils.tkinter_utils import center_resize_window

DEFAULT_COLUMN_WIDTH_PX = 140
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 100

class BookMainView(ttk.Frame):
    def __init__(self, parent, book_controller: BookController,
                 show_add_book_command: ShowAddBookCommand,
                 edit_book_command: ShowEditBookCommand, delete_books_command: DeleteBooksCommand):
        super().__init__(parent, padding="3 3 12 12")
        self.show_add_book_command = show_add_book_command
        self.edit_book_command = edit_book_command
        self.delete_books_command = delete_books_command
        self.book_controller = book_controller
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

        items = book_controller.get_all_books()
        self.item_list = ItemList(self, items)
        self.grid(column=0, row=0, sticky="nsew")

        # resize the parent window to show treeview widget
        self.item_list.update_idletasks()
        print(self.item_list.winfo_width(), self.item_list.winfo_height())
        center_resize_window(parent,
                             self.item_list.winfo_width(),
                             self.item_list.winfo_height() + BUTTONS_PANEL_HEIGHT_PX)

        # add buttons
        buttons_frame = ttk.Frame(self, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=1, sticky="nsew")
        self.add_button = ttk.Button(buttons_frame, text="Add Book", padding=10,
                                     command=self.show_add_book_command)
        self.add_button.grid(column=1, row=0, sticky=(N,E), padx=40, pady=20)

        self.add_button = ttk.Button(buttons_frame, text="Edit Book", padding=10,
                                     command=self.edit_book_command)
        self.add_button.grid(column=2, row=0, sticky=(N,E), padx=40, pady=20)
        self.add_button = ttk.Button(buttons_frame, text="Delete Books", padding=10,
                                     command=self.show_add_book_command)
        self.add_button.grid(column=3, row=0, sticky=(N,E), padx=40, pady=20)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col,minsize=300, pad=30)

    def refresh(self):
        books = self.book_controller.get_all_books()
        self.item_list.set_items(books)

