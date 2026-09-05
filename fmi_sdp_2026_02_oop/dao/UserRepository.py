from xml.dom.minidom import Entity

from exception.non_exisiting_entity_exception import NonExistingEntityException

class UserRepository:
    def __init__(self, id_generator):
        self.id_generator = id_generator
        self.entities: dict[str, Entity] = {}
    def __len__(self):
        return len(self.entities)
    def __iter__(self):
        return iter(self.entities.values())
    def create(self, entity):
        entity.id = self.id_generator.generate_id()
        self.entities[entity.id] = entity
        return entity
    def update(self, entity):
        if entity.id not in self.entities:
            raise NonExistingEntityException(f'Entity {type(entity)} with ID={entity.id} does not exist')
        self.entities[entity.id] = entity
        return entity
    def find_by_id(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        return None
    def find(self):
        return self.entities.values()
    def delete(self, entity_id):
        if entity_id not in self.entities:
            raise NonExistingEntityException(f'Entity with ID={entity_id} does not exist')
        return self.entities.pop(entity_id)