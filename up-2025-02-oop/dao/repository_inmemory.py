from typing import TypeVar

from dao.id_generator import IdGenerator
from dao.repository import Repository

class RepositoryInMemory[T](Repository):
    def __init__(self, id_generator: IdGenerator):
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

