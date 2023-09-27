from __future__ import annotations

from collections import deque
from typing import Iterator


class TreeNode:
    def __init__(self, data, children=None, parent = None):
        self.data = data
        self.parent = parent
        self.children = [] if children is None else children
        for child in self.children:
            child.parent = self

    def __repr__(self):
        result = str(self.data)
        if len(self.children) > 0:
            children_str = ', '.join(map(lambda child: str(child), self.children))
            result += f'({children_str})'
        return result

    def __len__(self):
        return len(self.children)

    def add_child(self, child: TreeNode) -> None:
        child.parent = self
        self.children.append(child)

    def add_children(self, children: list[TreeNode]) -> None:
        for child in children:
            self.add_child(child)


class Tree:
    def __init__(self, root=None):
        self.root: TreeNode = root

    def __str__(self):
        return str(self.root)

    def __iter__(self):
        return self.dfs_pre()

    def size(self):
        count = 0
        for node in self:
            count += 1
        return count

    def dfs_pre(self) -> Iterator[TreeNode]:
        stack = deque()
        if self.root is None:
            return
        stack.append(self.root)
        while len(stack) > 0:
            node: TreeNode = stack.pop()
            #previsit
            yield node
            for child in node.children:
                stack.append(child)

    def find_node_dfs(self, value):
        for node in self.dfs_pre():
            if node.data == value:
                return node
        return None

if __name__ == '__main__':
    t = Tree(TreeNode('A'))
    t.root.add_children([TreeNode('B', [TreeNode('C'), TreeNode('D'), TreeNode('E')]), TreeNode('F', [TreeNode('G'), TreeNode('H')])])
    print(t)
    t.find_node_dfs('D').add_children([TreeNode('X', [TreeNode('V'), TreeNode('W')]), TreeNode('Y')])
    print(t)
    print(f'Size: {t.size()}')

