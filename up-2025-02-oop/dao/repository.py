from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Generic repository interface
    """
    @abstractmethod
    def add(self, entity):
        """
        Adds an entity to the repository.
        :param entity: new entity to be added.
        :return: entity added with defined id
        """
        pass
    @abstractmethod
    def edit(self, entity):
        """
        Edits an entity in the repository.
        :param entity: entity to be edited.
        :return: the edited entity
        """
        pass
    @abstractmethod
    def delete(self, entity_id):
        """
        Deletes an entity from the repository.
        :param entity_id: id of the entity to be deleted.
        :return: deleted entity
        """
        pass
    @abstractmethod
    def find_by_id(self, entity_id):
        """
        Finds an entity by its id.
        :param entity_id: id of the entity to be found.
        :return: entity found
        """
        pass
    @abstractmethod
    def find_all(self):
        """
        Finds all entities in the repository.
        :return: all entities
        """
        pass