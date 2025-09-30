from abc import ABC
from typing import Callable, Set
from typing import Iterator

from myqueue import Queue
from mystack import StackLL
from queue_ll import QueueLL
from stack import Stack
from tree import BinaryTree, TreeVisitOrder

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

    def __len__(self):
        return self.size

    def __iter_subtree_dfs(self, root: BTNode) -> Iterator[BTNode[T]]:
        if root is None:
            return
        yield root
        yield from self.__iter_subtree_dfs(root.left)
        yield from self.__iter_subtree_dfs(root.right)

    def __iter__(self) -> Iterator[T]:
        return map(lambda node: node.val, self.__iter_subtree_dfs(self.root))

    def _traverse_dfs_rtl(self, visitor: Callable[[BTNode[T], int, int], bool], root: BTNode = None, depth: int = 0,
                          child_index: int = -1) -> int:
        if root is None:
            root = self.root
        if root is None:
            return False
        cont = visitor(root, depth, child_index)
        if cont and root.right is not None:
            cont = self._traverse_dfs_rtl(visitor, root.right, depth + 1, 1)
        if cont and root.left is not None:
            cont = self._traverse_dfs_rtl(visitor, root.left, depth + 1, 0)
        return cont

    def __str__(self):
        result = ''

        def visit_node(node: BTNode, depth: int, is_right: bool) -> bool:
            nonlocal result
            if is_right:
                result += f'{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            else:
                if node.parent.right is None:
                    result += 'None'
                result += f'\n{' ' * (ELEMENT_WIDTH + 2) * depth}{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            return True

        self._traverse_dfs_rtl(visit_node)
        return result

    def _find(self, val: T, root: BTNode = None) -> tuple[BTNode[T], bool, int]:
        if root is None:
            root = self.root
        if root is None:
            return None, False, -1
        if root.val == val:
            return root, True, -1
        if val < root.val:
            if root.left is not None:
                return self._find(val, root.left)
            else:
                return root, False, 0
        if val > root.val:
            if root.right is not None:
                return self._find(val, root.right)
            else:
                return root, False, 1

    def _find_max_node(self, root: BTNode[T] = None) -> BTNode[T]:
        if root is None:
            root = self.root
        while root.right is not None:
            root = root.right
        return root

    def _find_min_node(self, root: BTNode[T] = None) -> BTNode[T]:
        if root is None:
            root = self.root
        while root.left is not None:
            root = root.left
        return root

    def left_child(self, val: T) -> T:
        node, found, _ = self._find(val)
        if found:
            return node.left

    def right_child(self, val: T) -> T:
        node, found, _ = self._find(val)
        if found:
            return node.right

    def parent(self, val: T) -> T:
        node, found, _ = self._find(val)
        if found:
            return node.parent

    def sibling(self, val: T) -> T:
        node, found, child_index = self._find(val)
        if found:
            if child_index == 0:
                return node.parent.right
            elif child_index == 1:
                return node.parent.left

    def size(self) -> int:
        return self.size

    def tree_depth(self, root_val: T = None) -> int:
        max_depth = 0
        def visit_node(node: BTNode, depth: int, is_right: bool) -> bool:
            nonlocal max_depth
            if depth > max_depth:
                max_depth = depth
            return True

        if root_val is None:
            root_node, found = self.root, True
        else:
            root_node, found, _ = self._find(root_val)
        if found:
            self._traverse_dfs_rtl(visit_node, root_node)
            return max_depth

    def node_depth(self, val: T = None) -> int:
        node, found, _ = self._find(val)
        if found:
            depth = 0
            while node is not None:
                depth += 1
                node = node.parent
            return depth

    def add(self, val: T) -> BTNode[T]:
        if self.root is None:
            self.root = BTNode(val)
            return self.root
        node, found, child_index = self._find(val, self.root)
        if found:
            node.val = val
        else:
            new_node = BTNode(val, node)
            if child_index == 0:
                node.left = new_node
            else:
                node.right = new_node
            self.size += 1

    def _remove(self, val: T, root: BTNode[T]) -> BTNode[T]:
        if root is None:
            return None
        node, found, _ = self._find(val, root)
        if found:
            if node.left is not None:
                max_node = self._find_max_node(node.left)
                node.val = max_node.val
                self._remove(max_node.val, node.left)
            elif node.right is not None:
                min_node = self._find_min_node(node.right)
                node.val = min_node.val
                self._remove(min_node.val, node.right)
            else:
                if node.parent is None:
                    self.root = None
                if node.parent.left == node:
                    node.parent.left = None
                if node.parent.right == node:
                    node.parent.right = None
            return node

    def remove(self, val: T) -> BTNode[T]:
        return self._remove(val, self.root)

    def exists(self, val: T) -> T:
        node, found, _ = self._find(val, self.root)
        return found

    def is_leaf(self, val: T) -> bool:
        node, found, _ = self._find(val, self.root)
        if found:
            node.is_leaf()

    def _iter_dfs_nodes(self, order:TreeVisitOrder = TreeVisitOrder.PREORDER, ltr: bool = True) -> Iterator[T]:
        stack: Stack[BTNode[T]] = StackLL()
        visited: Set[BTNode[T]] = set()
        if self.root is None:
            return
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.peek()
            if order == TreeVisitOrder.PREORDER or node in visited:
                node = stack.pop()
                yield node

            if not node.is_leaf() and not node in visited:
                if ltr:
                    if node.right is not None:
                        stack.push(node.right)
                    if node.left is not None:
                        stack.push(node.left)
                else:
                    if node.left is not None:
                        stack.push(node.left)
                    if node.right is not None:
                        stack.push(node.right)
            visited.add(node)

    def iter_dfs(self, order: TreeVisitOrder = TreeVisitOrder.PREORDER, ltr: bool = True) -> Iterator[BTNode[T]]:
        return (node.val for node in self._iter_dfs_nodes(order, ltr))

    def _iter_bfs_nodes(self, ltr: bool = True) -> Iterator[T]:
        queue: Queue[BTNode[T]] = QueueLL()
        if self.root is None:
            return
        queue.enqueue(self.root)
        while not queue.is_empty():
            node = queue.dequeue()
            yield node

            if not node.is_leaf():
                if ltr:
                    if node.left is not None:
                        queue.enqueue(node.left)
                    if node.right is not None:
                        queue.enqueue(node.right)
                else:
                    if node.right is not None:
                        queue.enqueue(node.right)
                    if node.left is not None:
                        queue.enqueue(node.left)

    def iter_bfs(self, ltr: bool) -> Iterator[T]:
        return (node.val for node in self._iter_bfs_nodes(ltr))


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
    # t.remove(5)
    print(t)
    print(t.tree_depth(2))

    print('______________________________')
    for node in t._iter_bfs_nodes(False):
        print(node.val, end=' ')