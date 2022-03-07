import tkinter as tk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("300x200")

# box 1
box1 = tk.Label(
    root,
    text="Box 1",
    bg="green",
    fg="white",
)

box1.pack(
    ipadx=10,
    ipady=10,
    fill='x'
)

# box 2
box2 = tk.Label(
    root,
    text="Box 2",
    bg="red",
    fg="white"
)

box2.pack(
    ipadx=10,
    ipady=10,
    side='left',
    fill='y'
)

# box 3
box3 = tk.Label(
    root,
    text="Box 3",
    bg="yellow",
    fg="black"
)

box3.pack(
    ipadx=10,
    ipady=10,
    side='bottom',
    fill='x'
)

# box 4
box4 = tk.Label(
    root,
    text="Box 4",
    bg="blue",
    fg="white"
)

box4.pack(
    ipadx=10,
    ipady=10,
    side='right',
    expand=True,
    fill='both'
)

root.mainloop()
