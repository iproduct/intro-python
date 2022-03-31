from typing import Iterator

from exception.entity_not_found_exception import EntityNotFoundException


class RepositoryIterator(Iterator):
    """Iterates the repository elements"""
    def __init__(self, iterable):
        self._nextIndex = 0
        self._values = list(iterable)

    def __next__(self):
        if self._nextIndex < len(self._values):
            result = self._values[self._nextIndex]
            self._nextIndex += 1
            return result
        raise StopIteration


class Repository:
    """Provides lifecycle (CRUD) operations for specific type of entity"""
    def __init__(self, idGenerator):
        """Initializes the repository with provided idGenerator as dependency"""
        self._entities: dict = {}
        self._idGenrator = idGenerator

    def __len__(self):
        return self.count()

    def __add__(self, other):
        self._entities.update(other._entities)
        return self

    def __iter__(self):
        #return iter(self._entities.values())
        # return RepositoryIterator(self._entities.values())
        for entity in self._entities.values():
            yield entity

    def find_all(self):
        """Returns all entities in the repository"""
        return self._entities.values()

    def find_by_id(self, id):
        """
        Find entity with specific id
        :param id: id of the entity to return
        :return: the entity with specified id
        """
        found = self._entities.get(id)
        if found is None:
            raise EntityNotFoundException(f'Entity with ID:{id} not found')
        return found

    def create(self, entity):
        """
        Created new entity in the repository and assigns it a unique id using idGenrator provided in __init__()
        :param entity: entity to be created
        :return: created new entity with assignes
        """
        entity.id = self._idGenrator.get_next_id()
        self._entities[entity.id] = entity
        return entity

    def update(self, entity):
        self.find_by_id(entity.id)
        self._entities[entity.id] = entity
        return entity

    def delete_by_id(self, id):
        old = self.find_by_id(id)
        del self._entities[id]
        return old

    def count(self):
        return len(self._entities)
