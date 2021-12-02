from tkinter import *
from tkinter import ttk, messagebox

from utils.tkinter_utils import print_hierarchy

WIDTH = 800
HEIGHT = 600

class Application:
    def __init__(self, root):
        root.title("My Library")
        # Get the current screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Print the screen size
        print("Screen width:", screen_width)
        print("Screen height:", screen_height)

        left = (screen_width - WIDTH) // 2
        top = (screen_height - HEIGHT) // 2

        root.geometry(f"{WIDTH}x{HEIGHT}+{left}+{top}")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S) )

        menubar = Menu(root)
        root['menu'] = menubar
        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label="File")

        # File menu
        menu_file.add_command(label="New", command = self.newFile)


    def newFile(self):
        messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

if __name__ == '__main__':
    root = Tk()
    Application(root)
    print_hierarchy(root)
    root.mainloop()

