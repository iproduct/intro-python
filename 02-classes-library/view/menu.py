
class Command:
    def run(self) -> str:
        return "Not implemented"


class MenuItem:
    def __init__(self, text: str, command: Command):
        self.text = text
        self.command = command


class Menu:
    def __init__(self, items: list[MenuItem]):

        self.items = items
        self.items.append(MenuItem("Exit", lambda: ""))

    def show(self):
        while True:
            print("MAIN MENU:")
            for i, item in enumerate(self.items):
                print(f"{i:2d}: {item.text}")
            try:
                choice = int(input("Choose an option:"))
                if choice == len(self.items):  # last option should always be 'Exit'
                    break
                item = self.items[choice]
                print(item.command())
            except (ValueError, IndexError):
                print(f"Error: Please choose a valid option betwen 1 and {len(self.items)}")
                continue
