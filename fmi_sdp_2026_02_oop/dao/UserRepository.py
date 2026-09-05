class UserRepository:
    def __init__(self, id_generator):
        self.id_generator = id_generator
        self.entities = {}
    def create(self, entity):
        entity.id = self.id_generator.generate_id()
        self.entities[entity.id] = entity
        return entity
    def update(self, entity):
        if self.entities[entity.id] is None:
            raise NonExistingEntityException(f'Entity {type(entity)}')
            self.entities[entity.id] = entity
