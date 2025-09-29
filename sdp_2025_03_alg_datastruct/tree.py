from abc import ABC, abstractmethod

class BinaryTree[T](ABC):
    def root(self) -> T:
            pass
    @abstractmethod
    def left_child(self, val: T) -> T:
            pass
    @abstractmethod
    def right_child(self, val: T) -> T:
            pass
    @abstractmethod
    def parent(self, val: T) -> T:
            pass
    @abstractmethod
    def sibling(self, val: T) -> T:
            pass
    @abstractmethod
    def size(self) -> int:
            pass
    @abstractmethod
    def depth(self, val: T) -> int:
            pass
    @abstractmethod
    def add(self, val:T):
            pass
    @abstractmethod
    def remove(self, val:T):
            pass
    @abstractmethod
    def find(self, val: T) -> T:
            pass
    @abstractmethod
    def is_leaf(self, val: T) -> bool:
        pass