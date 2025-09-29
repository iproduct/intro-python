from abc import ABC
from typing import Callable
from typing import Iterator

from tree import BinaryTree

ELEMENT_WIDTH = 6


class BTNode[T]:
    def __init__(self, val: T, parent: 'BTNode[T]' = None, left: 'BTNode[T]' = None, right: 'BTNode[T]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f'[{str(self.val)} L: {str(self.left)}, R: {str(self.right)}]'

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None


class BinaryTreeLinked[T](BinaryTree[T]):
    def __init__(self):
        self.root = None
        self.size = 0

    def __iter_subtree_dfs(self, root: BTNode) -> Iterator[BTNode[T]]:
        yield root
        yield from self.__iter_subtree(root.left)
        yield from self.__iter_subtree(root.right)

    def __iter__(self) -> Iterator[T]:
        return map(lambda node: node.val, self.__iter_subtree_dfs(self.root))

    def _traverse_dfs_rtl(self, visitor: Callable[[BTNode[T], int, int], bool], root: BTNode = None, depth: int = 0, child_index: int = -1) -> int:
        if root is None:
            root = self.root
        cont = visitor(root, depth, child_index)
        if cont and root.right is not None:
            cont = self._traverse_dfs_rtl(visitor, root.right, depth + 1, 1)
        if cont and root.left is not None:
            cont = self._traverse_dfs_rtl(visitor, root.left, depth + 1, 0)
        return cont

    def __str__(self):
        prev_depth = 0
        result = ''
        def visit_node(node: BTNode, depth: int, is_right: bool) -> bool:
            nonlocal prev_depth
            nonlocal result
            if is_right:
                result += f'{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            else:
                if node.parent.right is None:
                    result += 'None'
                result += f'\n{' ' * (ELEMENT_WIDTH + 2) * depth}{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            prev_depth = depth
            prev_node = node
            return True
        self._traverse_dfs_rtl(visit_node)
        return result

    def _find(self, root: BTNode, val: T) -> tuple[BTNode[T], bool, int]:
        if root.val == val:
            return root, True
        if val < root.val:
            if root.left is not None:
                return self._find(root.left, val)
            else:
                return root, False, 0
        if val > root.val:
            if root.right is not None:
                return self._find(root.right, val)
            else:
                return root, False, 1

    def left_child(self, val: T) -> T:
        pass

    def right_child(self, val: T) -> T:
        pass

    def parent(self, val: T) -> T:
        pass

    def sibling(self, val: T) -> T:
        pass

    def size(self) -> int:
        pass

    def depth(self, val: T) -> int:
        pass

    def add(self, val: T) -> BTNode[T]:
        if self.root is None:
            self.root = BTNode(val)
            return self.root
        node, found, child_index = self._find(self.root, val)
        if found:
            node.val = val
        else:
            new_node = BTNode(val, node)
            if child_index == 0:
                node.left = new_node
            else:
                node.right = new_node


    def remove(self, val: T):
        pass

    def find(self, val: T) -> T:
        pass

    def is_leaf(self, val: T) -> bool:
        pass

if __name__ == '__main__':
    t = BinaryTreeLinked()
    t.add(5)
    t.add(10)
    t.add(2)
    t.add(1)
    t.add(3)
    t.add(42)
    t.add(41)
    t.add(11)

    print(t)