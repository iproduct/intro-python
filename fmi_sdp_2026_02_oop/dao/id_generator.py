import uuid
from typing import Protocol


class IdGenerator[IDType] (Protocol):
    def generate_id(self) -> IDType:
        ...

class IdGeneratorUuid(IdGenerator[uuid.UUID]):
    def generate_id(self) -> uuid.UUID:
        return uuid.uuid4()
