from tkinter import *
from tkinter import ttk

from controller.book_controller import BookController
from controller.calculator_controller import CalculatorController
from view.command.books.add_book_command import AddBookCommand
from view.command.books.list_books_command import ListBooksCommand
from view.command.exit_command import ExitCommand
from view.command.feet_to_meters_command import FeetToMetersCommand
from view.command.load_data_command import LoadDataCommand
from view.command.save_data_command import SaveDataCommand
from view.utils.tkinter_utils import print_hierarchy


class MainView(ttk.Frame):
    def __init__(self, root,
                 calc_controller: CalculatorController,
                 book_controller: BookController):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.calc_controller = calc_controller
        self.book_controller = book_controller

        # Create models
        self.feet = StringVar() # View Models (following MVVM architecture)
        self.meters = StringVar() # View Models (following MVVM architecture)

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

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Books", underline=0)
        menu_books.add_command(label="Add Book", command=AddBookCommand(book_controller))
        menu_books.add_command(label="List Books", command=ListBooksCommand(book_controller))





        self.createWidgets()
        print_hierarchy(root)

    def createWidgets(self):
        self.root.title('Feet to Meters Convertor')
        self.grid(column=0, row=0, sticky=(N, W, E, S))




        feet_entry = ttk.Entry(self, width=7, textvariable=self.feet)
        feet_entry.grid(column=1, row=1, columnspan=2, ipadx=15, ipady=15, sticky=(W, E))

        ttk.Label(self, textvariable=self.meters).grid(column=1, row=2, sticky=(W, E))

        # ttk.Button(self, text="Calculate", command=partial(self.calculate, suffix="m")).grid(column=3, row=3, sticky=(W))
        # ttk.Button(self, text="Calculate", command=lambda *args, **kwargs: self.calculate("m", *args, **kwargs))\
        ttk.Button(self, text="Calculate", command=FeetToMetersCommand(self.calc_controller)).grid(column=2, row=3, sticky=(W, N))
        self.bind_all("<Return>", FeetToMetersCommand(self.calc_controller))


        for child in self.winfo_children():
            child.grid_configure(padx=50, pady=10)

        rows, cols = self.grid_size()
        print(rows, cols)
        for row in range(rows):
            self.rowconfigure(row, weight=1, minsize=30, pad=30)
        for col in range(cols):
            self.columnconfigure(col, weight=1, minsize=50, pad=30)

    # def calculate(self, suffix="m"):
    #     try:
    #         self.meters.set(str(self.service.feet_to_meters(self.feet.get())) + suffix)
    #     except ValueError:
    #         self.show_error_dialog()

