import Tkinter as tk

class Application(tk.Frame): 3
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
    self.grid()
    self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)

self.quitButton.grid()
app = Application()
app.mainloop()
