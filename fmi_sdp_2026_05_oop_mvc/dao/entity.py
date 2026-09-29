from typing import Protocol


class Entity[IDType](Protocol):
    id: IDType