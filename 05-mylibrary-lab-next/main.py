from tkinter import *
from tkinter import ttk, messagebox

from utils.tkinter_utils import print_hierarchy

MAIN_WIDTH = 800
MAIN_HEIGHT = 600
DIALOG_WIDTH = 600
DIALOG_HEIGHT = 500

class Application:
    def __init__(self, root):
        root.title("My Library")
        print(f"Windowing system: {root.tk.call('tk', 'windowingsystem')}") # return  x11, win32, aqua
        root.option_add('*tearOff', FALSE) # remove menu tear off ability
        # Get the current screen width and height
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Print the screen size
        print("Screen width:", self.screen_width)
        print("Screen height:", self.screen_height)

        left, top = self._ceter_window_left_top(MAIN_WIDTH, MAIN_HEIGHT)

        root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}+{left}+{top}")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S) )

        self.menubar = Menu(root)
        root['menu'] = self.menubar


        # File menu
        menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label="File", underline=0)
        menu_file.add_command(label='New', command = self.newFile, underline=0, accelerator="Alt+N")
        self.mainframe.bind("<Alt-N>", self.newFile)
        print(menu_file.entryconfigure(0))
        menu_file.add_command(label="Open ...", command = self.openFile)
        menu_file.add_command(label='Close', command = self.closeFile)
        menu_file.entryconfigure('Close', state=DISABLED)

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Books", underline=0)
        menu_books.add_command(label='New', command=self.onNewBook, underline=0)


    def newFile(self):
        messagebox.showinfo(title="New File Dialog", message="Creating DB file ...")

    def openFile(self):
        messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

    def closeFile(self):
        messagebox.showinfo(title="File Close Dialog", message="Closing DB file ...")

    def onNewBook(self, *args):
        book_dlg = Toplevel(self.mainframe)
        left, top = self._ceter_window_left_top(DIALOG_WIDTH, DIALOG_HEIGHT)
        book_dlg.geometry(f"{DIALOG_WIDTH}x{DIALOG_HEIGHT}+{left}+{top}")
        book_dlg.wait_window()

    def _ceter_window_left_top(self, width, height):
        return ((self.screen_width - width) // 2, (self.screen_height - height) // 2)

if __name__ == '__main__':
    root = Tk()
    Application(root)
    print_hierarchy(root)
    root.mainloop()

