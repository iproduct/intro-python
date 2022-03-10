from tkinter import *
from tkinter import ttk

from controller.book_controller import BookController
from controller.calculator_controller import CalculatorController
from view.command.books.add_book_command import AddBookCommand
from view.command.books.delete_books_command import DeleteBooksCommand
from view.command.books.edit_book_command import ShowEditBookCommand
from view.command.books.list_books_command import ListBooksCommand
from view.command.books.show_add_book_command import ShowAddBookCommand
from view.command.exit_command import ExitCommand
from view.command.load_data_command import LoadDataCommand
from view.command.save_data_command import SaveDataCommand
from view.components.books_main_view import BookMainView
from view.utils.tkinter_utils import print_hierarchy


class MainView(ttk.Frame):
    def __init__(self, root, book_controller: BookController):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.book_controller = book_controller

        # Set root
        self.root.title('Feet to Meters Convertor')
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # Create menus
        self.menubar = Menu(root)
        root['menu'] = self.menubar
        # print(root.tk.call('tk', 'windowingsystem'))  # returns x11, win32 or aqua
        root.option_add('*tearOff', False)

        # File menu
        menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label="File", underline=0)
        menu_file.add_command(label="Load Data", command=LoadDataCommand(book_controller))
        menu_file.add_command(label="Save Data", command=SaveDataCommand(book_controller))
        menu_file.add_separator()
        exit_command = ExitCommand(root)
        menu_file.add_command(label="Exit", command=exit_command, underline=1, accelerator='Ctrl-Shift-X')
        root.bind_all("<Control-Shift-KeyPress-X>", exit_command )

        # Create commands
        self.show_add_book_command = ShowAddBookCommand(book_controller)
        self.show_edit_book_command = ShowEditBookCommand(book_controller)
        self.delete_books_command = DeleteBooksCommand(book_controller)
        self.list_books_command = ListBooksCommand(book_controller)

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Books", underline=0)
        menu_books.add_command(label="List Books", command=self.list_books_command)
        menu_books.add_separator()
        menu_books.add_command(label="Add Book", command=self.show_add_book_command)
        menu_books.add_command(label="Edit Book", command=self.show_edit_book_command)
        menu_books.add_command(label="Delete Books", command=self.delete_books_command)


        # Show items
        self.item_list = BookMainView(self.root, self.book_controller,
                                      self.show_add_book_command,
                                      self.show_edit_book_command,
                                      self.delete_books_command)

        print_hierarchy(root)

    def refresh(self):
        self.item_list.refresh()