from tkinter import Tk


class ExitCommand:
    def __init__(self, root: Tk):
        self.root = root

    def __call__(self, *args, **kwargs):
        self.root.destroy()
        print("Thank you for usint Book Catalog. Have a nice day!")
        exit(0)