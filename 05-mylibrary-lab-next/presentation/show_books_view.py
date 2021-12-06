from tkinter import *
from tkinter import ttk

from dao.book_repository import BookRepository

DEFAULT_COLUMN_WIDTH_PX = 100

class  ShowBooksView(ttk.Frame):
    def __init__(self, parent, label="", *args, entity_cls, books_repo: BookRepository):
        super().__init__(parent, *args, padding="3 3 12 12")
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # define headings
        columns = tuple(entity_cls().__dict__.keys())
        tree = ttk.Treeview(self, columns=columns, show='headings')
        for column in columns:
            print(column.title(), end=",")
            tree.heading(column, text=column.title())
            tree.column(column, width=DEFAULT_COLUMN_WIDTH_PX)

        tree.grid(row=0, column=0, sticky=NSEW)
        self.update_idletasks()
        parent.geometry(f"{tree.winfo_width() + 10}x{tree.winfo_height() + 200}")

        # # adding an item
        # tree.insert('', END, values=('John', 'Doe', 'john.doe@email.com'))
        #
        # # insert a the end
        # tree.insert('', END, values=('Jane', 'Miller', 'jane.miller@email.com'))
        #
        # # insert at the beginning
        # tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))