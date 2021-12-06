from tkinter import *
from tkinter import ttk, messagebox

from dao.book_repository_json import BookRepositoryJson
from model.book import Book
from utils.tkinter_utils import get_ceter_window_left_top

DIALOG_WIDTH = 600
DIALOG_HEIGHT = 500


class AddBookDialog:
    def __init__(self, parent, width=DIALOG_WIDTH, height=DIALOG_HEIGHT, *args, books_repo: BookRepositoryJson):
        self.books_repo = books_repo
        self.parent = parent
        self.book_dlg = Toplevel(self.parent, *args)
        self.book_dlg.title("Add Book")
        left, top = get_ceter_window_left_top(parent, width, height)
        self.book_dlg.geometry(f"{DIALOG_WIDTH}x{DIALOG_HEIGHT}+{left}+{top}")
        self.mainframe = ttk.Frame(self.book_dlg, padding="20 20 20 20")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # form model fields
        self.id = StringVar()
        self.title = StringVar()
        self.subtitle = StringVar()

        # form labels
        ttk.Label(self.mainframe, text="ID", justify=CENTER).grid(column=0, row=0, sticky=(E, W))
        ttk.Label(self.mainframe, text="Title", justify=CENTER).grid(column=0, row=1, sticky=(E, W))
        ttk.Label(self.mainframe, text="Subtitle", justify=CENTER).grid(column=0, row=2, sticky=(E, W))

        # form Entries
        self.id_entry = ttk.Entry(self.mainframe, textvariable=self.id, width=40).grid(column=1, row=0, sticky=(E, W))
        self.title_entry = ttk.Entry(self.mainframe, textvariable=self.title, width=40).grid(column=1, row=1,
                                                                                             sticky=(E, W))
        self.id_entry = ttk.Entry(self.mainframe, textvariable=self.subtitle, width=40).grid(column=1, row=2,
                                                                                             sticky=(E, W))

        # error message labels
        self.id_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')
        self.id_errors.grid(column=2, row=0, sticky=(E, W))
        self.title_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')
        self.title_errors.grid(column=2, row=1, sticky=(E, W))
        self.subtitle_errors = Label(self.mainframe, text="", justify=LEFT, fg='red')
        self.subtitle_errors.grid(column=2, row=2, sticky=(E, W))

        # buttons
        self.submit_button = ttk.Button(self.mainframe, text="Submit", command=self.onSubmit)
        self.submit_button.grid(column=1, row=3, sticky=(E))
        self.submit_button = ttk.Button(self.mainframe, text="New Dialog", command=self.onNewDialog)
        self.submit_button.grid(column=2, row=3, sticky=(E))


        # button = tk.Button(parent, text=text, font=(font), bg=bg, fg=fg, bd=bd, width=width, command=function)
        # button.grid(row=row, column=col, rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.book_dlg.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.book_dlg.transient(self.parent )
        self.book_dlg.wait_visibility()
        self.book_dlg.grab_set()
        self.book_dlg.wait_window()

    def onSubmit(self):
        book = Book(self.id.get(), self.title.get(), self.subtitle.get())
        self.books_repo.insert(book)
        self.books_repo.persist()
        self.dismiss()

    def onNewDialog(self):
        self.child_dialog = AddBookDialog(self.book_dlg, books_repo= self.books_repo)

    def dismiss(self):
        self.book_dlg.grab_release()
        self.book_dlg.destroy()