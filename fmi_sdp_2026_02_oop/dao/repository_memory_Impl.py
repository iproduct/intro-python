from typing import Iterator, Iterable, TypeVar, Any

from dao.abstract_repository import AbstractRepository
from dao.entity import Entity
from dao.id_generator import IdGenerator
from exception.non_exisiting_entity_exception import NonExistingEntityException


class RepositoryMemoryImpl[IDType, EntityType:Entity](AbstractRepository[IDType, EntityType]):
    def __init__(self, id_generator: IdGenerator[IDType]):
        self.id_generator = id_generator
        self.entities: dict[IDType, EntityType] = {}

    def __len__(self) -> int:
        return len(self.entities)

    def __iter__(self) -> Iterator[EntityType]:
        return iter(self.entities.values())

    def create(self, entity:EntityType) -> EntityType:
        entity.id = self.id_generator.generate_id()
        self.entities[entity.id] = entity
        return entity

    def update(self, entity: EntityType) -> EntityType:
        if entity.id not in self.entities:
            raise NonExistingEntityException(f'Entity {type(entity)} with ID={entity.id} does not exist')
        self.entities[entity.id] = entity
        return entity

    def find_by_id(self, entity_id: IDType) -> EntityType | None:
        if entity_id in self.entities:
            return self.entities[entity_id]
        return None

    def find(self) -> Iterable[EntityType]:
        return self.entities.values()

    def delete(self, entity_id: IDType) -> EntityType:
        if entity_id not in self.entities:
            raise NonExistingEntityException(f'Entity with ID={entity_id} does not exist')
        return self.entities.pop(entity_id)

    def size(self) -> int:
        return len(self.entities)
