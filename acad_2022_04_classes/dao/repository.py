from exception.entity_not_found_exception import EntityNotFoundException


class Repository:
    def __init__(self, idGenerator):
        self._entities = {}
        self._idGenrator = idGenerator

    def __len__(self):
        return self.count()

    def __add__(self, other):
        self._entities.update(other._entities)
        return self

    def find_all(self):
        return self._entities.values()

    def find_by_id(self, id):
        found = self._entities.get(id)
        if found is None:
            raise EntityNotFoundException(f'Entity with ID:{id} not found')
        return found

    def create(self, entity):
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
