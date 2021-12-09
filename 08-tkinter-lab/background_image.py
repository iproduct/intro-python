# Import module
from tkinter import *

if __name__ == "__main__":
    # Create object
    root = Tk()

    # Adjust size
    root.geometry("400x400")

    # Add image file
    bg = PhotoImage(file="Python-Programming.png")

    # Create Canvas
    canvas1 = Canvas(root, width=400,
                     height=400)

    canvas1.pack(fill="both", expand=True)

    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    # Add Text
    canvas1.create_text(200, 250, text="Welcome")

    # Create Buttons
    button1 = Button(root, text="Exit")
    button3 = Button(root, text="Start")
    button2 = Button(root, text="Reset")

    # Display Buttons
    button1_canvas = canvas1.create_window(100, 10,
                                           anchor="nw",
                                           window=button1)

    button2_canvas = canvas1.create_window(100, 40,
                                           anchor="nw",
                                           window=button2)

    button3_canvas = canvas1.create_window(100, 70, anchor="nw",
                                           window=button3)

    # Execute tkinter
    root.mainloop()

