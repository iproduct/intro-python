from enum import Enum
from json import dump, load
import uuid

from contact import PhoneType
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
            Item("Add contact", self.input_contact_handler),
            Item("Exit", self.exit_handler),
        ])

    def run(self):
        # self.load_contacts()
        while True:
            handler = self.menu.show()
            handler()

    def save_contacts(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            dump(self.contacts, f, indent=4, default=dumper)

    def load_contacts(self):
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            self.contacts = load(f)

    # Handlers
    def input_contact_handler(self):
        contact = self.input_view.input_contact()
        contact.id = uuid.uuid4()
        self.contacts.append(contact)
        print(self.contacts)
        self.save_contacts()

    def exit_handler(self):
        self.save_contacts()
        print('Good bye - have a nice day!')
        exit(0)


def dumper(obj):
    if isinstance(obj, Enum):
        return {
            '_class': obj.__class__.__name__,
            "value": obj.name
        }
    elif isinstance(obj, uuid.UUID):
        return {
            '_class': obj.__class__.__name__,
            "value": str(obj)
        }
    else:
        result = dict(obj.__dict__)
        result.update({"_class": obj.__class__.__name__})
        return result


def obj_hook(jsondict):
    pass
    # obj = cls()
    # del jsdict['_class']
    # obj.__dict__ = jsdict
    # return obj


if __name__ == '__main__':
    input_contact_view = InputContactView()
    ctrl = MainController('contacts.json', input_contact_view)
    ctrl.run()
