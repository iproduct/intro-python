from typing import Callable

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


class Item:
    def __init__(self, label: str, handler: Callable[[], None]):
        self.label = label
        self.handler = handler


class Menu:
    def __init__(self, items: list[Item]):
        self.items = items

    def show(self) -> Callable[[], None]:
        print()
        for i, item in enumerate(self.items, start=1):
            print(f'{i:>1d}: {item.label}')
        while True:
            try:
                choice = int(input("Choose an option: ")) - 1
            except ValueError:
                print('Not a number - try again.')
            if 0 <= choice < len(self.items):
                break
            print('Invalid choice - try again.')
        return self.items[choice].handler
