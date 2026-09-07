from abc import ABC, abstractmethod
from typing import Protocol, Iterable

from dao.entity import Entity


class AbstractRepository[IDType, EntityType](Protocol):
    def create(self, entity: EntityType[IDType]):
        ...

    def update(self, entity: EntityType[IDType]):
        ...

    def find_by_id(self, entity_id: IDType)-> EntityType[IDType]:
        ...

    def find(self)-> Iterable[EntityType[IDType]]:
        ...

    def delete(self, entity_id: IDType)-> EntityType[IDType]:
        ...

    def size(self) -> int:
        ...




