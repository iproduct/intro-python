from abc import ABC, abstractmethod


class Queue[T](ABC):
    @abstractmethod
    def enqueue(self, value:T) -> None:
        pass
    @abstractmethod
    def dequeue(self) -> T:
        pass
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    @abstractmethod
    def peek(self) -> T:
        pass
    @abstractmethod
    def size(self) -> int:
        pass