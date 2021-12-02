import tkinter


if __name__ == '__main__':
    import tkinter

    # Let's create the Tkinter window
    window = tkinter.Tk()
    window.title("GUI")

    # You will create two text labels namely 'username' and 'password' and and two input labels for them

    tkinter.Label(window, text="Username").grid(row=0)  # 'username' is placed on position 00 (row - 0 and column - 0)

    # 'Entry' class is used to display the input-field for 'username' text label
    tkinter.Entry(window).grid(row=0, column=1)  # first input-field is placed on position 01 (row - 0 and column - 1)

    tkinter.Label(window, text="Password").grid(row=1)  # 'password' is placed on position 10 (row - 1 and column - 0)

    tkinter.Entry(window).grid(row=1, column=1)  # second input-field is placed on position 11 (row - 1 and column - 1)

    # 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
    tkinter.Checkbutton(window, text="Keep Me Logged In").grid(columnspan=2)

    window.mainloop()