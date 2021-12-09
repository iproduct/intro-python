from functools import partial
from tkinter import *
from tkinter import ttk

DEFAULT_COLUMN_WIDTH_PX = 100


class ShowItemsView(ttk.Frame):
    def __init__(self, parent, items=[], add_command=lambda:None, edit_command=lambda:None, delete_command=lambda:None, *args, item_class):
        super().__init__(parent, *args, padding="3 0 0 0")
        self.__add_command = add_command
        self.__edit_command = edit_command
        self.__delete_command = delete_command
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # define headings
        columns = tuple(item_class().__dict__.keys())
        self.tree = ttk.Treeview(self, columns=columns, selectmode='extended', show='headings')
        for column in columns:
            print(column.title(), end=",")
            self.tree.heading(column, text=column.title())
            self.tree.column(column, width=DEFAULT_COLUMN_WIDTH_PX)

        self.tree.grid(row=0, column=0, sticky=NSEW)

        # add a vertical scrollbar
        vsb = ttk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky=(N, W, S), padx=0)
        self.tree.configure(yscrollcommand=vsb.set)

        # resize the parent window to show the treeview widget
        self.update_idletasks()
        parent.geometry(f"{self.tree.winfo_width() + 25}x{self.tree.winfo_height() + 200}")

        # set initial items in the treeview
        self.set_items(items)

        # add buttons
        buttons_frame = ttk.Frame(parent, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        self.add_button = ttk.Button(buttons_frame, text="Add Book", padding=10, command=self.__add_command)
        self.add_button.grid(column=0, row=0, sticky=(E), padx=40, pady=20)
        self.edit_button = ttk.Button(buttons_frame, text="Edit Book", padding=10, command=partial(self.process_items, self.__edit_command))
        self.edit_button.grid(column=1, row=0, sticky=(E), padx=40, pady=20)
        self.delete_button = ttk.Button(buttons_frame, text="Delete Books", padding=10, command=partial(self.process_items, self.__delete_command))
        self.delete_button.grid(column=2, row=0, sticky=(E), padx=40, pady=20)

    def set_items(self, items):
        if hasattr(self, "book_pos_ids"):
            self.tree.delete(*self.book_pos_ids)
        self.book_pos_ids = list(map(
            lambda book: self.tree.insert('', END, values=tuple(book.__dict__.values())),
            items)
        )
        self.update_idletasks()
        self.tree.see(self.book_pos_ids[-1])

    def process_items(self, command):
        items = []
        for selected_item in self.tree.selection():
            items.append(self.tree.item(selected_item, 'values'))
        print(items)
        command(items)

