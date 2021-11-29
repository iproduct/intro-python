from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value *1000.0 + 0.5) / 1000.0)
    except ValueError:
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("Feet to Meters Calculator")

    mainframe = ttk.Frame(root, padding="50 30 50 30")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # MVC - Model
    feet = StringVar() # input model
    meters = StringVar() # output model

    feet_entry = ttk.Entry(mainframe, width = 7, textvariable=feet) # bind model to view
    feet_entry.grid(column=2, row=1, sticky=(W, E))

    meter_label = ttk.Label(mainframe, textvariable= meters) # bind model to view
    meter_label.grid(column=2, row=2, sticky=(W, E))

    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=(E))
    ttk.Label(mainframe, text="feet").grid(column=3, row = 1, sticky=(W))
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=(W))

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=(W)) # bind Control function - Observer
    for child in mainframe.winfo_children():
        child.grid_configure(padx=15, pady=15)

    feet_entry.focus()
    root.bind("<Return>", calculate) # Observer: View -> Controller

    root.mainloop()