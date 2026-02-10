from typing import Protocol


class IdGenerator[IdType](Protocol):
    def get_next_id(self) -> IdType:
        ...