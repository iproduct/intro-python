from uuid import uuid4

from dao.id_generator import IdGenerator

class IdGenUuid(IdGenerator):
    def generate_id(self):
        return str(uuid4())
