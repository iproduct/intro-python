from abc import ABC, abstractmethod
from enum import Enum
from typing import Iterator

class TreeVisitOrder(Enum):
    PREORDER = 1
    POSTORDER = 2
    INORDER = 3

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
    def tree_depth(self, val: T) -> int:
            pass
    @abstractmethod
    def node_depth(self, val: T) -> int:
            pass
    @abstractmethod
    def add(self, val:T):
            pass
    @abstractmethod
    def remove(self, val:T):
            pass
    @abstractmethod
    def exists(self, val: T) -> bool:
            pass
    @abstractmethod
    def is_leaf(self, val: T) -> bool:
        pass
    @abstractmethod
    def iter_dfs(self, order: TreeVisitOrder, ltr: bool) -> Iterator[T]:
        pass
    @abstractmethod
    def iter_bfs(self, ltr: bool) -> Iterator[T]:
        pass

