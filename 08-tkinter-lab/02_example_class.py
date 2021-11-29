from tkinter import *
from tkinter import ttk

def print_hierarchy(w, depth = 0):
    print(
        '  ' * depth + w.winfo_class()
        + ' w=' + str(w.winfo_width()) + " h=" + str(w.winfo_height())
        + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y())
    )
    for chw in w.winfo_children():
        print_hierarchy(chw, depth+1)

class FeetToMeters:
    def __init__(self, root):
        root.title("Feet to Meters Calculator")
        self.mainframe = ttk.Frame(root, padding="50 30 50 30")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # MVC - Model
        self.feet = StringVar()  # input model
        self.meters = StringVar()  # output model

        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet)  # bind model to view
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        meter_label = ttk.Label(self.mainframe, textvariable=self.meters)  # bind model to view
        meter_label.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.mainframe, text="is equivalent to").grid(column=1, row=2, sticky=(E))
        ttk.Label(self.mainframe, text="feet").grid(column=3, row=1, sticky=(W))
        ttk.Label(self.mainframe, text="meters").grid(column=3, row=2, sticky=(W))

        # bind Control function - Observer pattern
        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=(W))
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.feet_entry.focus()
        # Observer: View -> Controller
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value *1000.0 + 0.5) / 1000.0)
        except ValueError:
            pass


if __name__ == '__main__':
    root = Tk()
    FeetToMeters(root)
    root.mainloop()