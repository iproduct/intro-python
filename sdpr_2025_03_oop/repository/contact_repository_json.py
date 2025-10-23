import json

from model.contact import Contact
from repository.contact_repository import ContactRepository
from repository.id_generator import IdGenerator


class ContactRepositoryJson(ContactRepository):
    def __init__(self, id_generator: IdGenerator, db_filename: str):
        super().__init__(id_generator)
        self.db_filename = db_filename

    def load(self):
        def object_hook(obj_dict: dict):
            obj = Contact()
            obj.__dict__.update(obj_dict)
            return obj
        with open(self.db_filename) as json_file:
            data = json.load(json_file, object_hook=object_hook)
            for contact in data:
                self.contacts[contact.id] = contact

