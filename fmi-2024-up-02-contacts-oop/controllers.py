from enum import Enum
from json import dump, load
import uuid

from contact import PhoneType, Phone, Contact
from menus import Menu, Item
from views import InputContactView, ShowContactsView


class MainController:
    def __init__(self, db_filename, input_contact_view: InputContactView, show_contacts_view: ShowContactsView):
        self.db_filename = db_filename
        self.input_contact_view = input_contact_view
        self.show_contacts_view = show_contacts_view
        self.contacts = []
        self.menu = self.create_menu()

    def create_menu(self):
        return Menu([
            Item("Print all contacts", self.show_contacts_handler),
            Item("Add contact", self.input_contact_handler),
            Item("Exit", self.exit_handler),
        ])

    def run(self):
        self.load_contacts()
        while True:
            handler = self.menu.show()
            handler()

    def save_contacts(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            dump(self.contacts, f, indent=4, default=dumper)

    def load_contacts(self):
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            self.contacts = load(f, object_hook=object_hook_factory({
                'PhoneType': PhoneType,
                'Phone': Phone,
                'Contact': Contact,
                'UUID': uuid.UUID
            }))

    # Handlers
    def show_contacts_handler(self):
        self.show_contacts_view.show(self.contacts)

    def input_contact_handler(self):
        contact = self.input_contact_view.show()
        contact.id = uuid.uuid4()
        self.contacts.append(contact)
        self.save_contacts()

    def exit_handler(self):
        # self.save_contacts()
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


def object_hook_factory(entity_classes_dict): #HOF, closure
    def obj_hook(jsondict):
        cls_name = jsondict['_class']
        cls = entity_classes_dict[cls_name]
        if issubclass(cls, Enum):
            return cls[jsondict['value']]
        elif cls_name == uuid.UUID.__name__:
            return uuid.UUID(jsondict['value'])
        else:
            obj = cls()
            del jsondict['_class']
            obj.__dict__ = jsondict
            return obj
    return obj_hook


if __name__ == '__main__':
    input_contact_view = InputContactView()
    show_contacts_view = ShowContactsView()
    ctrl = MainController('contacts.json', input_contact_view, show_contacts_view)
    ctrl.run()
