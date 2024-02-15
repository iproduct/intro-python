from json import dump, load


class MainController:
    def __init__(self, db_filename):
        self.db_filename = db_filename

    def run(self):
        # self.load_contacts()
        while True:
            choice = show_menu()
            MAIN_MENU[choice]['handler']()

    def save_contacts(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            dump(contacts, f, indent=4)

    def load_contacts(self):
        global contacts
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            contacts = load(f)
