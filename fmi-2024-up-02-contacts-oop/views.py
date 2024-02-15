import re

from contact import Contact, Phone, PhoneType


class InputContactView:
    def __init__(self):
        pass
    def show(self) -> Contact:
        contact = Contact()
        while True:
            contact.first = input('Input first name:')
            if len(contact.first) >= 1:
                break
            print('Fist name is mandatory. Try again.')
        while True:
            contact.last = input('Input last name:')
            if len(contact.last) >= 2:
                break
            print('Last name sholud be at least 2 characters long. Try again.')
        contact.address = input('Input address:') # optional
        complete = False
        while not complete:
            phone = Phone()
            while True:
                options = ', '.join([f'{pt.value} for {pt.name}' for pt in PhoneType])
                type_choice = input(f'Input phone type [{options}, ENTER to cancel]:')
                if type_choice == '':
                    complete = True
                    break
                try:
                    phone.type = PhoneType(int(type_choice))
                    break
                except ValueError:
                    print(f'Your chice should be a number 1 - {len(PhoneType)}. Try again.')
            while not complete:
                phone.number = input('Input phone number [ex. (03592) 123456]:')
                if re.match(r'^[\d\s()]{6,15}$', phone.number):
                    contact.phones.append(phone)
                    break
                print('Phone number should contain only digits, spaces and parenthesis (). Try again.')
        return contact

class ShowContactsView:
    def __init__(self):
        pass

    def show(self, contacts):
        print()
        for contact in contacts:
            print(contact)


if __name__ == '__main__':
    view = InputContactView()
    c = view.input_contact()
    print(c)