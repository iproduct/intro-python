from typing import Callable


class TreeNode:
    def __init__(self, val, parent=None, children=None):
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


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        result = ''

        def visit_node(node: TreeNode, depth: int, child_index: int) -> bool:
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
                              visitor: Callable[[TreeNode, int, int], bool],
                              root: TreeNode = None,
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

    def _insert_child(slef, parent_node: TreeNode, child_node: TreeNode):
        parent_node.children.append(child_node)
        child_node.parent = parent_node

    def insert(self, parent_val, child_val):
        pass

if __name__ == '__main__':
    root = TreeNode("C:")
    tree = Tree(root)
    dir1 = TreeNode("Progs")
    dir2 = TreeNode("Users")
    dir3 = TreeNode("Data")
    tree._insert_child(root, dir1)
    tree._insert_child(root, dir2)
    tree._insert_child(root, dir3)
    dir11 = TreeNode("Word")
    dir12 = TreeNode("Excel")
    tree._insert_child(dir1, dir11)
    tree._insert_child(dir1, dir12)
    dir21 = TreeNode("john")
    dir22 = TreeNode("jane")
    dir23 = TreeNode("ava")
    tree._insert_child(dir2, dir21)
    tree._insert_child(dir2, dir22)
    tree._insert_child(dir2, dir23)
    print(tree)
