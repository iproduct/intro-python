from contact import Contact, Phone


class InputContactView:
    def __init__(self):
        pass
    def input_contact(self) -> Contact:
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
        contact['phones'] = []
        complete = False
        while not complete:
            phone = Phone()
            while True:
                type_choice = input('Input phone type [1) for MOBILE, 2) for HOME 3) for WORK, ENTER to cancel]:')
                if type_choice == '':
                    complete = True
                    break
                try:
                    phone.type = PHONE_TYPES[int(type_choice)]
                except ValueError:
                    print(f'Your chice should be a number 1 - {len(PHONE_TYPES)}. Try again.')
                    continue
                if phone['type'] is None:
                    print(f'Your chice should be a number 1 - {len(PHONE_TYPES)}. Try again.')
                    continue
                break

            while not complete:
                phone['number'] = input('Input phone number [ex. (03592) 123456]:')
                if re.match('^[\d\s()]{6,15}$', phone['number']):
                    contact['phones'].append(phone)
                    break
                print('Phone number should contain only digits, spaces and parenthesis (). Try again.')
        return contact