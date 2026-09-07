from typing import Iterator, Iterable
from xml.dom.minidom import Entity

from dao.abstract_repository import AbstractRepository
from exception.non_exisiting_entity_exception import NonExistingEntityException


class RepositoryMemoryImpl[IDType, EntityType](AbstractRepository[IDType, EntityType]):
    def __init__(self, id_generator):
        self.id_generator = id_generator
        self.entities: dict[IDType, EntityType] = {}

    def __len__(self) -> int:
        return len(self.entities)

    def __iter__(self) -> Iterator[EntityType]:
        return iter(self.entities.values())

    def create(self, entity) -> EntityType:
        entity.id = self.id_generator.generate_id()
        self.entities[entity.id] = entity
        return entity

    def update(self, entity) -> EntityType:
        if entity.id not in self.entities:
            raise NonExistingEntityException(f'Entity {type(entity)} with ID={entity.id} does not exist')
        self.entities[entity.id] = entity
        return entity

    def find_by_id(self, entity_id) -> EntityType | None:
        if entity_id in self.entities:
            return self.entities[entity_id]
        return None

    def find(self) -> Iterable[EntityType]:
        return self.entities.values()

    def delete(self, entity_id) -> EntityType:
        if entity_id not in self.entities:
            raise NonExistingEntityException(f'Entity with ID={entity_id} does not exist')
        return self.entities.pop(entity_id)

    def size(self) -> int:
        return len(self.entities)
