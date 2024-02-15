from json import dump, load
from menus import Menu, Item


class MainController:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.menu = self.create_menu()

    @staticmethod
    def create_menu():
        return Menu([
            Item("Print all contacts", lambda: None),
            Item("Add contact", lambda: None),
            Item("Exit", lambda: None),
        ])

    def run(self):
        # self.load_contacts()
        while True:
            handler = self.menu.show()
            handler()


    def save_contacts(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            dump(contacts, f, indent=4)

    def load_contacts(self):
        global contacts
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            contacts = load(f)


if __name__ == '__main__':
    ctrl = MainController('contacts.json')
    ctrl.run()