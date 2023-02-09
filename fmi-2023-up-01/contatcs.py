from typing import Callable

def print_contacts():
    print(f'\nAll Contacts:')
    with open('contacts.csv', 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        parts = line.split(',')
        print(f'{parts[0].strip():20} | {parts[1].strip():15}')

def input_contact():
    print(f'\nAdd New Contact:')
    name = input('Name:')
    phone = input('Phone:')
    line = f'\n{name},{phone}'
    with open('contacts.csv', 'at', encoding='utf-8') as f:
        f.write(line)


def delete_contact():
    print(f'\nDelete Contact:')
    with open('contacts.csv', 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    for index, line in enumerate(lines):
        line = line.strip()
        parts = line.split(',')
        print(f'{index + 1} | {parts[0].strip():20} | {parts[1].strip():15}')
    selected = int(input('Select contact to delete:'))
    lines.pop(selected - 1)
    with open('contacts.csv', 'wt', encoding='utf-8') as f:
        f.writelines(lines)

def run_menu(options: list[tuple[str, Callable]]):
    while True:
        print()
        print('-'*20)
        for index, option in enumerate(options):
            print(f'{index + 1}: {option[0]}')
        print('-' * 20)
        selected = int(input('Select option:'))
        options[selected - 1][1]()

def finish():
    print('\nGoodbye from Personal Contacts program.')
    exit()

main_menu = [
    ('Print All Contacts', print_contacts),
    ('Add New Contact', input_contact),
    ('Delete Contact', delete_contact),
    ('Exit', finish)
]

if __name__ == '__main__':
    run_menu(main_menu)