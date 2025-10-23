import uuid

from repository.id_generator import IdGenerator


class UuidGenerator(IdGenerator):
    def get_next_id(self) -> str:
        return uuid.uuid4()