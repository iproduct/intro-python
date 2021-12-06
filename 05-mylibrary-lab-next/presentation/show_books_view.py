from tkinter import *
from tkinter import ttk

class  ShowBooksView(ttk.Frame):
    def __init__(self, parent, label="", *args):
        super().__init__(parent, *args, padding="3 3 12 12")
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        tree.grid(row=0, column=0, sticky=NSEW)

        # adding an item
        tree.insert('', END, values=('John', 'Doe', 'john.doe@email.com'))

        # insert a the end
        tree.insert('', END, values=('Jane', 'Miller', 'jane.miller@email.com'))

        # insert at the beginning
        tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))