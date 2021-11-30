from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    root = Tk()
    root.geometry("800x400")
    root.title("Feet to Meters Calculator")
    mainframe = ttk.Frame(root, padding="50 30 50 30")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    l = ttk.Label(mainframe, text="Starting ...", width=100)
    l.grid()

    mainframe.bind('<Enter>', lambda e: l.configure(text="Moved mouse inside."))
    mainframe.bind('<Leave>', lambda e: l.configure(text="Moved mouse outside."))
    mainframe.bind('<ButtonPress-1>', lambda e: l.configure(text="Clicked left mouse button."))
    mainframe.bind('<3>', lambda e: l.configure(text="Clicked right mouse button."))
    mainframe.bind('<Double-1>', lambda e: l.configure(text="Double clicked left mouse button."))
    mainframe.bind('<B3-Motion>', lambda e: l.configure(text=f"Dragged with right button to: {e.x}, {e.y}"))

    root.mainloop()