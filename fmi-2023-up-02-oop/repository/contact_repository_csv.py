from model.contact import Contact
from repository.contact_repository import ContactRepository


class ContactRepositoryCsv(ContactRepository):
    def load(self, filename):
        with open(filename, 'rt', encoding='utf-8') as f:
            self.contacts.clear()
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                parts = line.split(',')
                id = parts[0].strip()
                name = parts[1].strip()
                phone = parts[2].strip()
                self.contacts[id] = Contact(name, phone, id)

    def save(self, filename):
        with open(filename, 'wt', encoding='utf-8') as f:
            for c in self.contacts.values():
                f.write(f'{c.id},{c.name},{c.phone}\n')