from tkinter import *
from tkinter import ttk

from dao.book_repository import BookRepository
from model.book import Book

DEFAULT_COLUMN_WIDTH_PX = 100


class ShowBooksView(ttk.Frame):
    def __init__(self, parent, initial_books: list[Book] = [], *args, entity_cls, ):
        super().__init__(parent, *args, padding="3 0 0 0")
        self.books = initial_books
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # define headings
        columns = tuple(entity_cls().__dict__.keys())
        self.tree = ttk.Treeview(self, columns=columns, selectmode='browse', show='headings')
        for column in columns:
            print(column.title(), end=",")
            self.tree.heading(column, text=column.title())
            self.tree.column(column, width=DEFAULT_COLUMN_WIDTH_PX)

        self.tree.grid(row=0, column=0, sticky=NSEW)

        # add a vertical scrollbar
        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky=(N, W, S), padx=0)
        self.tree.configure(yscrollcommand=vsb.set)

        self.update_idletasks()
        parent.geometry(f"{self.tree.winfo_width() + 25}x{self.tree.winfo_height() + 200}")

        self._insert_books()

    def _insert_books(self) -> list[str]:
        if hasattr(self, "book_pos_ids"):
            self.tree.delete(*self.book_pos_ids)
        self.book_pos_ids = list(map(
            lambda book: self.tree.insert('', END, values=tuple(book.__dict__.values())),
            self.books)
        )
        self.update_idletasks()
        return self.book_pos_ids

    def refresh(self, books):
        self.books = books
        self._insert_books()


        # # adding an item
        # tree.insert('', END, values=('John', 'Doe', 'john.doe@email.com'))
        #
        # # insert a the end
        # tree.insert('', END, values=('Jane', 'Miller', 'jane.miller@email.com'))
        #
        # # insert at the beginning
        # tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))
