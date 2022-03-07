import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Treeview demo')
root.geometry('620x200')

# define columns
columns = ('first_name', 'last_name', 'email')

tree = ttk.Treeview(root, columns=columns, show='tree')

# define headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')


tree.column('#0', width=1, anchor=tk.W)
tree.column('first_name', width=100, anchor=tk.W)
tree.column('last_name', width=100, anchor=tk.E)
tree.column('email', width=200, anchor=tk.CENTER)

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

# add data to the treeview
for id, contact in enumerate(contacts, 1):
    print(tree.insert('', tk.END, iid=id, values=contact, open=False))

tree.insert('', tk.END, values=(f'John', f'Doe', f'john@example.com'), iid=200, open=False)
tree.insert('', tk.END, values=(f'Jane', f'Doe', f'jane@example.com'), iid=201, open=False)
tree.move(200, 1, 0)
tree.move(201, 1, 1)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


# tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')
root.rowconfigure(0, weight=1, minsize=300, pad=30)
root.columnconfigure(0, weight=1, minsize=300, pad=30)

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()