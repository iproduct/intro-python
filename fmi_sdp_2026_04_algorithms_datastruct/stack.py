from abc import ABC, abstractmethod
from typing import Protocol


class Stack(Protocol):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass