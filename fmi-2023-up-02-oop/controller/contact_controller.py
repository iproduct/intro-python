from model.contact import Contact
from repository.contact_repository_csv import ContactRepositoryCsv as ContactRepo


class ContactController:
    def __init__(self, filename, contact_repo):
        self.filename = filename
        self.repo = contact_repo

    def start(self):
        self.repo.create(Contact('Trayan Iliev', '0878-2345678'))
        self.repo.create(Contact('Maria Petrova', '08976789543'))
        self.repo.create(Contact('John Doe', '014567889995'))
        self.repo.save(self.filename)
        self.repo.load(self.filename)
        for cont in self.repo.find_all():
            print(cont)

if __name__ == '__main__':
    ctrl = ContactController('conacts.csv', ContactRepo()) # Constructor-based dependency injection
    ctrl.start()