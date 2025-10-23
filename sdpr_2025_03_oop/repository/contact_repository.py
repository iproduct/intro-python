from typing import List

from model.contact import Contact
from repository.id_generator import IdGenerator
from repository.uuid_generator import UuidGenerator


class ContactRepository:

    def __init__(self, id_generator: IdGenerator):
        self.id_generator = id_generator
        self.contacts = {}

    def create(self, contact: Contact) -> Contact:
        contact.id = self.id_generator.get_next_id()
        self.contacts[contact.id] = contact
        return contact

    def find_all(self) -> List[Contact]:
        return list(self.contacts.values())

if __name__ == '__main__':
    id_generator = UuidGenerator()
    repository = ContactRepository(id_generator)
    lc = [
        Contact('Trayan', 'Iliev', '0887543211', 't_iliev@gmial.com', 'Sofia, J.Bouchier 5'),
        Contact('Jane', 'Smith', '0883456211', 'jsmith@gmial.com', 'London'),
    ]
    for contact in lc:
        repository.create(contact)

    for contact in repository.find_all():
        print(contact)
