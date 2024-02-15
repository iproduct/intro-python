from json import dump, load
import uuid

from menus import Menu, Item
from views import InputContactView


class MainController:
    def __init__(self, db_filename, input_view: InputContactView):
        self.db_filename = db_filename
        self.input_view = input_view
        self.contacts = []
        self.menu = self.create_menu()

    def create_menu(self):
        return Menu([
            Item("Print all contacts", lambda: None),
            Item("Add contact", lambda: None),
            Item("Exit", self.exit_handler),
        ])

    def run(self):
        # self.load_contacts()
        while True:
            handler = self.menu.show()
            handler()

    def save_contacts(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            dump(self.contacts, f, indent=4)

    def load_contacts(self):
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            self.contacts = load(f)

    # Handlers
    def input_contact_handler(self):
        contact = self.input_view.input_contact()
        contact.id = uuid.uuid4()
        self.contacts.append(contact)
        self.save_contacts()

    def exit_handler(self):
        self.save_contacts()
        print('Good bye - have a nice day!')
        exit(0)


if __name__ == '__main__':
    ctrl = MainController('contacts.json')
    ctrl.run()
