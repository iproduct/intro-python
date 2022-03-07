import tkinter as tk

root = tk.Tk()
root.title('Tkinter place Geometry Manager')

# label 1
label1 = tk.Label(
    root,
    text="Absolute placement",
    bg='red',
    fg='white'
)

label1.place(x=20, y=10, width=200, height=150)

# label 2
label2 = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

label2.place(relx=0.5, rely=0.5, relwidth=0.5, anchor='center')

root.mainloop()