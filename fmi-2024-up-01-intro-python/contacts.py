import json
import re

CONTACTS_DB_FILE = 'contacts.json'

sample_contacts = [
    {
        "id": 1,
        "first": "Trayan",
        "last": "Iliev",
        "address": {
            "country": "BG",
            "city": "Sofia",
            "street": "Jamaes Bouchier Blvd., 42"
        },
        "phones": [
            {
                "type": "work",
                "number": "+3592895423"
            },
            {
                "type": "mobile",
                "number": "+359885167243"
            },
        ]
    },
    {
        "id": 2,
        "first": "Georgi",
        "last": "Spasov",
        "address": {
            "country": "BG",
            "city": "Plovdiv",
            "street": "Pet tepeta, 18"
        },
        "phones": [
            {
                "type": "work",
                "number": "+3594312345"
            },
            {
                "type": "mobile",
                "number": "+359889195572"
            },
        ]
    }
]

PHONE_TYPES = {
    1: 'MOBILE',
    2: 'HOME',
    3: 'WORK',
}

contacts = []

def format_contact(contact: dict) -> str:
    result = ''
    phones_str = ', '.join([f'{ph["type"]}: {ph["number"]}' for ph in contact['phones']])
    result += f'| {contact["id"]:>3d} | ' \
              f'{contact["first"] + " " + contact["last"]:<15.15s} | ' \
              f'{contact["address"]["street"] + ", " + contact["address"]["city"] + ", " + contact["address"]["country"]:<40.40s} | ' \
              f'{phones_str:40.40s} |'
    return result

def print_contacts(contacts):
    for contact in contacts:
        print(format_contact(contact))

def print_contacts_handler():
    print_contacts(contacts)


def save_contacts(db_filename):
    with open(db_filename, 'wt', encoding='utf-8') as f:
        json.dump(contacts, f, indent=4)


def load_contacts(db_filename):
    global contacts
    with open(db_filename, 'rt', encoding='utf-8') as f:
        contacts = json.load(f)

def exit_handler():
    save_contacts(CONTACTS_DB_FILE)
    print('Good bye - have a nice day!')
    exit(0)

def input_contact() -> dict:
    contact = dict()
    while True:
        contact['first'] = input('Input first name:')
        if len(contact['first']) >= 1:
            break
        print('Fist name is mandatory. Try again.')
    while True:
        contact['last'] = input('Input last name:')
        if len(contact['last']) >= 2:
            break
        print('Last name sholud be at least 2 characters long. Try again.')
    contact['address'] = dict()
    while True:
        country = input('Input country code [ENTER for BG]:').upper()
        if country == '':
            country = 'BG'
        if len(country) == 2:
            contact['address']['country'] = country
            break
        print('Country code should be two uppercase characters. Try again.')
    contact['address']['city'] = input('Input city:') # optional
    contact['address']['street'] = input('Input street address:') # optional
    contact['phones'] = []

    complete = False
    while not complete:
        phone = dict()
        while True:
            type_choice = input('Input phone type [1) for MOBILE, 2) for HOME 3) for WORK, ENTER to cancel]:')
            if type_choice == '':
                complete = True
                break
            try:
                phone['type'] = PHONE_TYPES[int(type_choice)]
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

def add_contact_handler():
    contact = input_contact()
    contact['id'] = contacts[-1]['id'] + 1
    contacts.append(contact)
    save_contacts(CONTACTS_DB_FILE)

MAIN_MENU = [
    {
        "label": "Print all contacts",
        "handler": print_contacts_handler,
    },
    {
        "label": "Add contact",
        "handler": add_contact_handler,
    },
    {
        "label": "Exit",
        "handler": exit_handler
    },
]

def show_menu() -> int:
    print()
    for i, option in enumerate(MAIN_MENU, start=1):
        print(f'{i:>1d}: {option["label"]}')
    while True:
        try:
            choice = int(input("Choose an option: ")) - 1
        except ValueError:
            print('Not a number - try again.')
        if 0 <= choice < len(MAIN_MENU):
            break
        print('Invalid choice - try again.')
    return choice


if __name__ == "__main__":
    # save_contacts(CONTACTS_DB_FILE) # uncomment to create db first time
    load_contacts(CONTACTS_DB_FILE)
    while True:
        choice = show_menu()
        MAIN_MENU[choice]['handler']()