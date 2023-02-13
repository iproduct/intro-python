from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
    from controller.contact_controller import ContactController

import re
from model.contact import Contact


class InputContactView():
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
            if re.match(r'^[\(\)\s\+\-\d]{6,20}$', phone):
                break
            print("Error: Phone must contain digits, whitespace, '(', ')', '+' and '-' only, between 6 and 15 long.")
        contact = Contact(name, phone)
        print(contact)