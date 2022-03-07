from tkinter import *
from tkinter import ttk, messagebox


def launchFindDialog(*args):
    messagebox.showinfo(message="I hope you find what you're looking for!")


def newFile(*args):
    messagebox.showinfo(message="Creating file ...")


def openFile(*args):
    messagebox.showinfo(message="Opening file ...")


def closeFile(*args):
    messagebox.showinfo(message="Closing file ...")


if __name__ == '__main__':
    root = Tk()
    print(root.tk.call('tk', 'windowingsystem'))  # returns x11, win32 or aqua
    root.option_add('*tearOff', False)

    win = Toplevel(root)
    ttk.Entry(win).grid()
    menubar = Menu(win)
    win['menu'] = menubar
    # menubar = Menu(root)
    # root['menu'] = menubar

    menu_file = Menu(menubar)
    menu_edit = Menu(menubar)
    menubar.add_cascade(menu=menu_file, label='File')
    menubar.add_cascade(menu=menu_edit, label='Edit')

    menu_file.add_command(label='New', command=newFile)
    menu_file.add_command(label='Open...', command=openFile)
    menu_file.add_command(label='Close', command=closeFile)

    menu_edit.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
    menu_edit.add_command(label='Find...', command=lambda: root.event_generate('<<OpenFindDialog>>'))
    root.event_add('<<OpenFindDialog>>', '<Button-3>')

    root.bind('<<OpenFindDialog>>', launchFindDialog)
    root.mainloop()