import json

from model.contact import Contact
from repository.contact_repository import ContactRepository
from repository.id_generator import IdGenerator
from repository.uuid_generator import UuidGenerator


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


    def save(self):
        def dumper(obj):
            return obj.__dict__
        with open(self.db_filename, 'wt') as json_file:
            json.dump(self.find_all(), json_file, indent=4, default=dumper)

if __name__ == '__main__':
    id_generator = UuidGenerator()
    repository = ContactRepositoryJson(id_generator, '../contacts.json')
    lc = [
        Contact('Trayan', 'Iliev', '0887543211', 't_iliev@gmial.com', 'Sofia, J.Bouchier 5'),
        Contact('Jane', 'Smith', '0883456211', 'jsmith@gmial.com', 'London'),
    ]
    for contact in lc:
        repository.create(contact)

    repository.save()
    repository.load()

    for contact in repository.find_all():
        print(contact)
