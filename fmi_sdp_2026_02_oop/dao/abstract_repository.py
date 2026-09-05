from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def create(self, entity):
        raise NotImplementedError()
    @abstractmethod
    def update(self, entity):
        raise NotImplementedError()
    @abstractmethod
    def find_by_id(self, entity_id):
        raise NotImplementedError()
    @abstractmethod
    def find(self):
        raise NotImplementedError()
    @abstractmethod
    def delete(self, entity_id):
        raise NotImplementedError()
    @abstractmethod
    def size(self):
        raise NotImplementedError()




