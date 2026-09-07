from abc import ABC, abstractmethod
from typing import Protocol, Iterable

from dao.entity import Entity


class AbstractRepository[IDType, EntityType](Protocol):
    @abstractmethod
    def create(self, entity: EntityType):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity: EntityType):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, entity_id: IDType)-> EntityType | None:
        raise NotImplementedError

    @abstractmethod
    def find(self)-> Iterable[EntityType]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id: IDType)-> EntityType:
        raise NotImplementedError

    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError




