from typing import Callable

def print_contacts():
    with open('contacts.csv', 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        parts = line.split(',')
        print(f'{parts[0].strip():20} | {parts[1].strip():15}')

def input_contact():
    name = input('Name:')
    phone = input('Phone:')
    line = f'\n{name},{phone}'
    with open('contacts.csv', 'at', encoding='utf-8') as f:
        f.write(line)

def run_menu(options: list[tuple[str, Callable]]):
    for index, option in enumerate(options):
        print(f'{index + 1}: {option[0]}')

def finish():
    print('Goodbye from Personal Contacts program.')
    exit()

main_menu = [
    ('Print All Contacts', print_contacts),
    ('Add New Contact', input_contact),
    ('Exit', finish)
]

if __name__ == '__main__':
    run_menu(main_menu)