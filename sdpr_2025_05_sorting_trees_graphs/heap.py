from abc import ABC, abstractmethod


class Heap[T](ABC):
    @abstractmethod
    def insert(self, value: T):
        pass
    @abstractmethod
    def extract(self) -> T:
        pass
    @abstractmethod
    def is_empty(self) -> bool:
        pass