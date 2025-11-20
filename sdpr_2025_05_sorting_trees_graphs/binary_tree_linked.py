from typing import Iterator, Callable

from binary_tree import BinaryTree


class BTNode[T]:
    def __init__(self, val: T, parent: 'BTNode[T]' = None, left: 'BTNode[T]'=None, right: 'BTNode[T]'=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return f'[{self.val}, P: {self.parent}, L: {self.left}, R: {self.right}]'

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_root(self):
        return self.parent is None

ELEMENT_WIDTH = 4

class BinaryTreeLinked[T](BinaryTree[T]):
    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        result = ''
        def visit_node(node: BTNode[T], depth: int, is_right: bool) -> bool:
            # print('====>', repr(node), depth, is_right)
            nonlocal result
            if is_right:
                result += f'{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            else:
                if node.parent.right is None:
                    result += 'None'
                result += f'\n{' ' * max((ELEMENT_WIDTH + 2) * depth - 2, 0)}->{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            return True
        self._traverse_dfs_pre_rtl(visit_node)
        return result

    def _traverse_dfs_pre_rtl(self,
                              visitor: Callable[[BTNode[T], int, bool], bool],
                              root: BTNode[T] = None,
                              depth: int = 0,
                              child_index: int = -1) -> bool:
        if root is None:
           root = self.root
        if root is None:
            return False
        cont = visitor(root, depth, child_index)
        if cont and root.right is not None:
            cont = self._traverse_dfs_pre_rtl(visitor, root.right, depth + 1, 1)
        if cont and root.left is not None:
            cont = self._traverse_dfs_pre_rtl(visitor, root.left, depth + 1, 0)
        return cont


    def _find(self, val: T, root: BTNode[T] = None) -> tuple[BTNode[T], bool]:
        if root is None:
            root = self.root
        if root is None:
            return None, False
        if root.val == val:
            return root, True
        if val < root.val:
            if root.left is None:
                return root, False
            return self._find(val, root.left)
        if  val > root.val:
            if root.right is None:
                return root, False
            return self._find(val, root.right)

    def root(self):
        return self.root

    def sibling(self, val: T) -> T:
        node, found = self._find(val)
        if found and node.parent is not None:
            parent = node.parent
            if parent.left == node:
                return parent.right
            else:
                return parent.left

    def size(self) -> int:
        pass

    def tree_depth(self, node: T) -> int:
        pass

    def node_depth(self, node: T) -> int:
        pass

    def add(self, val: T):
        if self.root is None:
            self.root = BTNode(val)
            return
        node, found = self._find(val)
        # print('====>find: ', repr(node), found)
        if found:
            node.val = val
        else:
            new_node = BTNode(val)
            new_node.parent = node
            if val < node.val:
                node.left = new_node
            else:
                node.right = new_node
        # print('====>find- return: ', repr(node), found)
        self.size = self.size + 1

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

if __name__ == '__main__':
    t = BinaryTreeLinked()
    t.add(5)
    t.add(10)
    t.add(2)
    t.add(1)
    t.add(4)
    t.add(42)
    t.add(41)
    t.add(11)
    t.add(3)
    t.add(9)

    print(t)


