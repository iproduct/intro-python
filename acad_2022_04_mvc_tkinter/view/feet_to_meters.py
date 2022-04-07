import functools
from tkinter import *
from tkinter import ttk

from view.command.exit_command import ExitCommand
from view.utils.tkinter_utils import center_resize_window


class FeetToMeters(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding="3 3 12 12")
        self.root = root

        # Set root
        center_resize_window(root)
        self.root.title('Feet to Meters Calculator')
        self.grid(column=0, row=0, sticky=NSEW)

        # Add child widgets
        btn_calc = ttk.Button(self, text='Calculate', command=lambda : print('Calculating...'))
        btn_calc = ttk.Button(self, text='Calculate', command=functools.partial(print, 'Calculating...'))
        btn_calc.grid(column=0, row=0, sticky=EW)
        btn_calc = ttk.Button(self, text='Exit', command=ExitCommand(self.root))
        btn_calc.grid(column=0, row=1, sticky=EW)

if __name__ =="__main__":
    root = Tk()
    FeetToMeters(root)
    root.mainloop()