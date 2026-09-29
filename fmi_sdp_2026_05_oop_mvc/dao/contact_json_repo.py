from enum import Enum
from json import dump, load
import uuid

from dao.id_generator import IdGenerator
from dao.repository_memory_Impl import RepositoryMemoryImpl
from model.contact import PhoneType, Phone, Contact
from view.menus import Menu, Item
from view.views import InputContactView, ShowContactsView


class ContactJsonRepo(RepositoryMemoryImpl[uuid.UUID, Contact]):
    def __init__(self, id_generator: IdGenerator[uuid.UUID], db_filename):
        super().__init__(id_generator)
        self.db_filename = db_filename

    def save_contacts(self):
        with open(self.db_filename, 'wt', encoding='utf-8') as f:
            dump(self.contacts, f, indent=4, default=dumper)

    def load_contacts(self):
        with open(self.db_filename, 'rt', encoding='utf-8') as f:
            self.contacts = load(f, object_hook=object_hook_factory({
                'PhoneType': PhoneType,
                'Phone': Phone,
                'Contact': Contact,
                'UUID': uuid.UUID
            }))


def dumper(obj):
    if isinstance(obj, Enum):
        return {
            '_class': obj.__class__.__name__,
            "value": obj.name
        }
    elif isinstance(obj, uuid.UUID):
        return {
            '_class': obj.__class__.__name__,
            "value": str(obj)
        }
    else:
        result = dict(obj.__dict__)
        result.update({"_class": obj.__class__.__name__})
        return result


def object_hook_factory(entity_classes_dict): #HOF, closure
    def obj_hook(jsondict):
        cls_name = jsondict['_class']
        cls = entity_classes_dict[cls_name]
        if issubclass(cls, Enum):
            return cls[jsondict['value']]
        elif cls_name == uuid.UUID.__name__:
            return uuid.UUID(jsondict['value'])
        else:
            obj = cls()
            del jsondict['_class']
            obj.__dict__ = jsondict
            return obj
    return obj_hook

