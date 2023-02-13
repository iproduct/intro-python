import re

from controller.contact_controller import ContactController
from model.contact import Contact


class InputContact():
    def __init__(self, controller: ContactController):
        self.controller = controller
    def show(self):
        print('INPUT NEW CONTACT')
        while True:
            name = input('Name: ').strip()
            if len(name) > 2:
                break
            print('Error: Name must be at least 3 characters long.')
        while True:
            phone = input('Phone: ')
            if re.match(r'^[(,),-,\d]{6,15}$', phone):
                break
            print("Error: Phone must contain digits, '(', ')' and '-' only, between 6 and 15 long.")
        contact = Contact(name, phone)
        print(contact)