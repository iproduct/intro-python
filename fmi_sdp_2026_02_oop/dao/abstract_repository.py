from abc import ABC, abstractmethod
from typing import Protocol

from dao.entity import Entity


class AbstractRepository[IDType](Protocol):
    def create(self, entity: Entity[IDType]):
        ...

    def update(self, entity: Entity[IDType]):
        ...

    def find_by_id(self, entity_id: IDType):
        ...

    def find(self):
        ...

    def delete(self, entity_id: IDType):
        ...

    def size(self):
        ...




