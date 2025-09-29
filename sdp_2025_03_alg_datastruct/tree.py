from abc import ABC, abstractmethod

class Tree[T](ABC):
    def root(self) -> T:
            pass
    @abstractmethod
    def left_child(self, node: T) -> T:
            pass
    @abstractmethod
    def right_child(self, node: T) -> T:
            pass
    @abstractmethod
    def parent(self, node: T) -> T:
            pass
    @abstractmethod
    def sibling(self, node: T) -> T:
            pass
    @abstractmethod
    def size(self) -> int:
            pass
    @abstractmethod
    def depth(self, node: T) -> int:
            pass
    @abstractmethod
    def add(self, node:T):
            pass
    @abstractmethod
    def remove(self, node:T):
            pass
    @abstractmethod
    def find(self, node: T) -> T:
            pass
    @abstractmethod
    def is_leaf(self, node: T) -> bool:
        pass