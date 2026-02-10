import uuid


class IdGeneratorUuid:
    def get_next_id(self) -> str:
        return str(uuid.uuid4())