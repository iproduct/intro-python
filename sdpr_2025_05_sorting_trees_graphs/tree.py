from collections import deque
from typing import Callable


class TreeNode[T]:
    def __init__(self, val: T, parent=None, children=None):
        if children is None:
            children = []
        self.val = val
        self.parent = parent
        self.children = children

    def __repr__(self):
        return f'[{self.val}, P:{self.parent}, C:{self.children}]'

    def __str__(self):
        return self.val

    def is_leaf(self):
        return len(self.children) == 0

    def is_root(self):
        return self.parent is None


ELEMENT_WIDTH = 5


class Tree[T]:
    def __init__(self, root: TreeNode[T] = None):
        self.root = root

    def __str__(self):
        result = ''

        def visit_node(node: TreeNode[T], depth: int, child_index: int) -> bool:
            # print('====>', repr(node), depth, is_right)
            nonlocal result
            if child_index == 0:
                result += f'{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            else:
                result += f'\n{' ' * max((ELEMENT_WIDTH + 2) * depth - 2, 0)}->{str(node.val).ljust(ELEMENT_WIDTH)}{"" if node.is_leaf() else "->"}'
            return True

        self._traverse_dfs_pre_rtl(visit_node)
        return result

    def _traverse_dfs_pre_rtl(self,
                              visitor: Callable[[TreeNode[T], int, int], bool],
                              root: TreeNode[T] = None,
                              depth: int = 0,
                              child_index: int = 0) -> bool:
        if root is None:
            root = self.root
        if root is None:
            return False
        cont = visitor(root, depth, child_index)
        for i, child in enumerate(root.children):
            if cont:
                cont = self._traverse_dfs_pre_rtl(visitor, child, depth + 1, i)
            else:
                break
        return cont

    def _insert_child(slef, parent_node: TreeNode[T], child_node: TreeNode[T]):
        parent_node.children.append(child_node)
        child_node.parent = parent_node

    def _find_first_node_bfs(self, predicate: Callable[[TreeNode[T]], bool]) -> TreeNode[T]:
        queue = deque()
        queue.appendleft(self.root)
        while queue:
            current = queue.pop()
            if predicate(current):
                return current
            for child in current.children:
                queue.appendleft(child)

    def insert(self, parent_val, child_val):
        parent = self._find_first_node_bfs(lambda node: node.val == parent_val)
        self._insert_child(parent, TreeNode(child_val))


if __name__ == '__main__':
    tnum = Tree(TreeNode(42))
    tnum.insert(42, 12)
    tnum.insert(42, 5)
    tnum.insert(42, 102)
    tnum.insert(5, 15)
    tnum.insert(5, 35)
    tnum.insert(102, 14)
    tnum.insert(102, 53)
    tnum.insert(53, 64)
    tnum.insert(53, 78)
    tnum.insert(102, 4)
    tnum.insert(12, 17)
    print(tnum)

    # root = TreeNode("C:")
    # tree = Tree(root)
    # dir1 = TreeNode("Progs")
    # dir2 = TreeNode("Users")
    # dir3 = TreeNode("Data")
    # tree._insert_child(root, dir1)
    # tree._insert_child(root, dir2)
    # tree._insert_child(root, dir3)
    # dir11 = TreeNode("Word")
    # dir12 = TreeNode("Excel")
    # tree._insert_child(dir1, dir11)
    # tree._insert_child(dir1, dir12)
    # dir21 = TreeNode("john")
    # dir22 = TreeNode("jane")
    # dir23 = TreeNode("ava")
    # tree._insert_child(dir2, dir21)
    # tree._insert_child(dir2, dir22)
    # tree._insert_child(dir2, dir23)
    # print(tree)
    # def is_jane(node: TreeNode) -> bool:
    #     return node.val == "jane"
    # def is_progs_ignore_case(node: TreeNode) -> bool:
    #     return node.val.lower() == "progs".lower()
    # users_dir = tree._find_first_node_bfs(is_progs_ignore_case)
    # # users_dir = tree._find_first_node_bfs(lambda node: node.val == "jane")
    # print(repr(users_dir))
