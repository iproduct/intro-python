from tkinter import *
from tkinter import ttk

DEFAULT_COLUMN_WIDTH_PX = 100
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 200


class ItemList(ttk.Frame):
    def __init__(self, items, parent):
        super().__init__(parent, padding="3 3 12 12")
        self.parent = parent
        self.items = items
        self.item_pos_ids = None
        self.grid(row=0, column=0, sticky='nsew')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

        columns = self.items[0].__dict__.keys();
        self.tree = ttk.Treeview(self, columns=columns,
                                 selectmode='extended', show='headings')
        for column in columns:
            self.tree.heading(column, column.title())
            self.tree.column(column, width=DEFAULT_COLUMN_WIDTH_PX)

        self.tree.grid(row=0, column=0, sticky= NSEW)

        #add vertical scrollbar
        vsb = ttk.Scrollbar(parent, orient=VERTICAL, command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky=(N, W, S), padx=0)
        self.tree.configure(yscroll=vsb.set)

        # resize the parent window to show treeview widget
        self.update_idletasks()
        parent.geometry(f"{self.tree.winfo_width() + SCROLLBAR_WIDTH_PX}x"
                + f"{self.tree.winfo_height() + BUTTONS_PANEL_HEIGHT_PX}")

        # set items
        self.set_items(self.items)

    def set_items(self, items):
        if self.item_pos_ids is not None:
            self.tree.delete(*self.item_pos_ids)
        self.item_pos_ids = list(map(
            lambda item: self.tree.insert('', END, values=tuple(item.__dict__.values())),
            self.items
        ))
        self.items = items
        self.update_idletasks()
        self.tree.see(self.item_pos_ids[-1])