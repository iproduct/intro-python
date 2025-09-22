import json
import os
from datetime import datetime
from enum import Enum
from typing import TypeVar

from dao.id_generator import IdGenerator
from dao.repository import Repository


class RepositoryJsonFile[T](Repository):
    def __init__(self, filename: str, id_generator: IdGenerator):
        self.filename = filename
        self.id_generator = id_generator
        self._entities = {}

    def __contains__(self, item: T) -> bool:
        return item in set(self._entities.values())

    def __iter__(self):
        return iter(self._entities.values())

    def __len__(self) -> int:
        return len(self._entities)

    def add(self, entity: T):
        entity.id = self.id_generator.generate_id()
        self._entities[entity.id] = entity
        self.save_to_file()
        return entity

    def edit(self, entity: T):
        self._entities[entity.id] = entity
        return entity

    def delete(self, entity_id):
        old = self.find_by_id(entity_id)
        del self._entities[entity_id]
        return old

    def find_by_id(self, entity_id):
        return self._entities[entity_id]

    def find_all(self):
        return list(self._entities.values())

    def load_from_file(self, overwrite: bool = False):
        pass

    def save_to_file(self):
        def _dumper(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Enum):
                return {
                    "__class": obj.__class__.__name__,
                    "value": obj.name
                }
            else:
                result = dict(obj.__dict__)
                result.update({"__class": obj.__class__.__name__})
                return result
        dir = os.path.dirname(self.filename)
        if dir:
            os.makedirs(dir, exist_ok=True)
        self.load_from_file()
        with open(self.filename, 'w') as f:
            json.dump(self._entities, f, indent=4, default=_dumper)

