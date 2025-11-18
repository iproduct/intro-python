from typing import Iterator

from binary_tree import BinaryTree


class BTNode[T]:
    def __init__(self, val: T, parent: 'BTNode[T]' = None, left: 'BTNode[T]'=None, right: 'BTNode[T]'=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
    def __str__(self):
        return self.val
    def __repr__(self):
        return f'[{self.val}, P: {self.parent}, L: {self.left}, R: {self.right}]'

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_root(self):
        return self.parent is None

class BinaryTreeLinked[T](BinaryTree[T]):
    def __init__(self):
        self.root = None
        self.size = 0

    def _find(self, val: T, root: BTNode[T] = None) -> tuple[BTNode[T], bool]:
        if root is None:
            root = self.root
        if root is None:
            return None, False
        if root.val == val:
            return root, True
        if root.val < val:
            if root.left is None:
                return root, False
            return self._find(val, root.left)
        if root.val > val:
            if root.right is None:
                return root, False
            return self._find(val, root.right)

    def root(self):
        return self.root

    def sibling(self, node: T) -> T:
        pass

    def size(self) -> int:
        pass

    def tree_depth(self, node: T) -> int:
        pass

    def node_depth(self, node: T) -> int:
        pass

    def add(self, node: T):
        pass

    def remove(self, node: T):
        pass

    def exists(self, node: T) -> bool:
        pass

    def is_leaf(self, node: T) -> bool:
        pass

    def is_root(self, node: T) -> bool:
        pass

    def iter_dfs(self) -> Iterator[T]:
        pass

    def iter_bfs(self) -> Iterator[T]:
        pass



