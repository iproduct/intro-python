from abc import ABC, abstractmethod
from typing import Protocol, Iterable

from dao.entity import Entity


class AbstractRepository[IDType, EntityType](Protocol):
    def create(self, entity: EntityType):
        ...

    def update(self, entity: EntityType):
        ...

    def find_by_id(self, entity_id: IDType)-> EntityType | None:
        ...

    def find(self)-> Iterable[EntityType]:
        ...

    def delete(self, entity_id: IDType)-> EntityType:
        ...

    def size(self) -> int:
        ...




