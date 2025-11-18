from abc import ABC, abstractmethod
from typing import Iterator


class BinaryTree[T](ABC):
    @abstractmethod
    def root(self):
        pass
    @abstractmethod
    def sibling(self, node:T) -> T:
        pass
    @abstractmethod
    def size(self) -> int:
        pass
    @abstractmethod
    def tree_depth(self, node:T) -> int:
        pass
    @abstractmethod
    def node_depth(self, node:T) -> int:
        pass
    @abstractmethod
    def add(self, node:T):
        pass
    @abstractmethod
    def remove(self, node:T):
        pass
    @abstractmethod
    def exists(self, node:T) -> bool:
        pass
    @abstractmethod
    def is_leaf(self, node:T) -> bool:
        pass
    @abstractmethod
    def is_root(self, node:T) -> bool:
        pass
    @abstractmethod
    def iter_dfs(self) -> Iterator[T]:
        pass
    @abstractmethod
    def iter_bfs(self) -> Iterator[T]:
        pass

