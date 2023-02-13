from __future__ import annotations

from model.contact import Contact
from presentation.input_contact_view import InputContactView
from repository.contact_repository_csv import ContactRepositoryCsv as ContactRepo


class ContactController:
    def __init__(self, filename, contact_repo):
        self.filename = filename
        self.repo = contact_repo

    def create_new_contact(self, contact: Contact):
        self.repo.create(contact)
        self.repo.save()

    def start(self):
        self.repo.create(Contact('Trayan Iliev', '0878-2345678'))
        self.repo.create(Contact('Maria Petrova', '08976789543'))
        self.repo.create(Contact('John Doe', '014567889995'))
        self.repo.save(self.filename)
        self.repo.load(self.filename)
        for cont in self.repo.find_all():
            print(cont)
        input_contact_view = InputContactView(self)
        input_contact_view.show()

if __name__ == '__main__':
    ctrl = ContactController('conacts.csv', ContactRepo()) # Constructor-based dependency injection
    ctrl.start()