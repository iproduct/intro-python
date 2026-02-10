from collections.abc import Callable
from typing import Any

from dao.id_gen_uuid import IdGeneratorUuid
from dao.id_generator import IdGenerator
from model.contact import Contact


class ContactRepository:
    def __init__(self, id_generator: IdGenerator[str]) -> None:
        self.id_generator = id_generator
        self.contacts: dict[str, Contact] = {}

    def create(self, contact: Contact) -> Contact:
        contact.id = self.id_generator.get_next_id()
        self.contacts[contact.id] = contact
        return contact

    def find_all(self, key_func: Callable[[Contact], Any] = None) -> list[Contact]:
        results = list(self.contacts.values())
        if key_func:
            results.sort(key=key_func)
        return results

if __name__=="__main__":
    contacts_repo = ContactRepository(IdGeneratorUuid())
    lc = [
        Contact('Trayan', 'Iliev',  't_iliev@gmial.com', '0887543211','Sofia, J.Bouchier 5'),
        Contact('Jane', 'Smith', 'jsmith@gmial.com', '0883456211', 'London'),
    ]
    for contact in lc:
        contacts_repo.create(contact)

    for contact in contacts_repo.find_all(lambda contact: contact.last_name):
        print(contact)
