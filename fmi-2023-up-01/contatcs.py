from typing import Callable

def print_contacts():
    print(f'\nAll Contacts:')
    get_print_contacts()

def get_print_contacts():
    with open('contacts.csv', 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    for index, line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            continue
        parts = line.split(',')
        print(f'{index + 1} | {parts[0].strip():20} | {parts[1].strip():15}')
    return lines

def input_contact():
    print(f'\nAdd New Contact:')
    name = input('Name:')
    phone = input('Phone:')
    line = f'\n{name},{phone}'
    with open('contacts.csv', 'at', encoding='utf-8') as f:
        f.write(line)

def delete_contact():
    print(f'\nDelete Contact:')
    lines = get_print_contacts()
    selected = int(input('Select contact to DELETE:'))
    lines.pop(selected - 1)
    with open('contacts.csv', 'wt', encoding='utf-8') as f:
        f.writelines(lines)

def edit_contact():
    print(f'\nEdit Contact:')
    lines = get_print_contacts()
    selected = int(input('Select contact to EDIT:'))
    line = lines[selected - 1]
    parts = line.split(',')
    name = parts[0].strip()
    phone  = parts[1].strip()
    new_name = input(f'Name [{name} - <Enter to keep>]:').strip()
    if len(new_name) == 0:
        new_name = name
    new_phone = input(f'Phone [{phone} - <Enter to keep>]:').strip()
    if len(new_phone) == 0:
        new_phone = phone
    lines[selected - 1] = f'{new_name},{new_phone}\n'
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