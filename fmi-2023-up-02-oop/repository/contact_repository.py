from typing import Iterable
from model.contact import Contact
from uuid import uuid4


class ContactRepository:
    def __init__(self):
        self.contacts = dict()

    def find_all(self) -> Iterable[Contact]:
        return self.contacts.values()

    def find_by_id(self, id: str):
        return self.contacts[id]

    def create(self, contact: Contact):
        contact.id = uuid4()
        self.contacts[contact.id] = contact
        return contact

    def update(self, contact):
        self.contacts[contact.id] = contact
        return contact

    def delete_by_id(self, id: str):
        deleted = self.contacts[id]
        del(self.contacts[id])
        return deleted

    def count(self):
        return len(self.contacts)