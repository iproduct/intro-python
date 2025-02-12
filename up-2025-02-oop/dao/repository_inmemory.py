from dao.id_generator import IdGenerator
from dao.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self, id_generator: IdGenerator):
        self.id_generator = id_generator
        self.entities = {}

    def add(self, entity):
        entity.id = self.id_generator.generate_id()
        self.entities[entity.id] = entity
        return entity

    def edit(self, entity):
        self.entities[entity.id] = entity
        return entity

    def delete(self, entity_id):
        old = self.find_by_id(entity_id)
        del self.entities[entity_id]
        return old

    def find_by_id(self, entity_id):
        return self.entities[entity_id]

    def find_all(self):
        return list(self.entities.values())

