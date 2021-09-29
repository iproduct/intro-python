from typing import Callable, Iterable

from abstract_tree import AbstractTree
from queue import LifoQueue, Queue

class TreeNode:
    def __init__(self, data=None, parent=None, children=()):
        self.data = data
        self.parent = parent
        self.children = list(children)

    def __str__(self):
        result = str(self.data)
        if len(self.children) > 0:
            result += '('
            length = len(self.children)
            for i in range(length):
                result += str(self.children[i]) + (',' if i < length - 1 else '')
            result += ')'
        return result

    def __len__(self):
        count = 1
        for child in self.children:
            count += len(child)
        return count

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def add_children(self, *children):
        for child in children:
            child.parent = self
        self.children.extend(children)

class Tree(AbstractTree):
    def __init__(self, root = None):
        if root == None:
            self.__root = TreeNode()
        else:
            self.__root = root
        self.__size = 1

    def __str__(self):
        return f'({str(self.__root)})'

    @property
    def root(self) -> TreeNode:
        return self.__root

    @property
    def size(self):
        return self.__size

    def is_root(self, node: TreeNode) -> bool:
        return node is self.root

    def is_leaf(self, node: TreeNode) -> bool:
        return len(node.children) == 0

    def is_internal(self, node: TreeNode) -> bool:
        return not self.is_root() and not self.is_leaf()

    def add_child(self, parent_node: TreeNode, child_node: TreeNode):
        parent_node.add_child(child_node)
        self.__size += len(child_node)

    def add_children(self,  parent_node: TreeNode, *children):
        parent_node.add_children(*children)
        for child in children:
            self.__size += len(child)

    def find(self, value) -> list[TreeNode]:
        predicate = lambda tree_node: tree_node.data == value
        return self.find_by_predicate(predicate, self.root)

    def find_first(self, value) -> list[TreeNode]:
        predicate = lambda tree_node: tree_node.data == value
        return self.find_first_by_predicate(predicate, self.root)

    def find_by_predicate(self, predicate: Callable[[TreeNode], bool], start_node: TreeNode = None) -> list[TreeNode]:
        results = [] # recursion bottom
        if start_node != None:
            if predicate(start_node):
                results.append(start_node)
            for child in start_node.children:
                results.extend(self.find_by_predicate(predicate, child)) # recursion step
        return results

    def find_first_by_predicate(self, predicate: Callable[[TreeNode], bool], start_node: TreeNode = None) -> TreeNode:
        result = None  # recursion bottom
        if start_node != None:
            if predicate(start_node):
                return start_node
            for child in start_node.children:
                found = self.find_first_by_predicate(predicate, child) # recursion step
                if found != None:
                    return found
        return result

    # search iterators
    def nodes_dfs_preorder(self):
        return TreeNodePreDFSIterator(self)

    def nodes_bfs_preorder(self):
        return TreeNodePreBFSIterator(self)

    def nodes_bfs_postorder(self):
        return TreeNodePostBFSIterator(self)


# Helper classes
class TreeNodePreDFSIterator:
    def __init__(self, tree: Tree):
        self.tree = tree
    def __iter__(self):
        stack = LifoQueue()
        stack.put(self.tree.root)
        while not stack.empty():
            node = stack.get()
            yield node
            for index in range(len(node.children) - 1, -1, -1): # reverse children
                stack.put(node.children[index])

class TreeNodePreBFSIterator:
    def __init__(self, tree: Tree):
        self.tree = tree
    def __iter__(self):
        stack = Queue()
        stack.put(self.tree.root)
        while not stack.empty():
            node = stack.get()
            yield node
            for child in node.children:
                stack.put(child)

class TreeNodePostBFSIterator:
    def __init__(self, tree: Tree):
        self.tree = tree
    def __iter__(self):
        queue = Queue()
        yield_stack = LifoQueue()
        queue.put(self.tree.root)
        while not queue.empty():
            node = queue.get()
            yield_stack.put(node)
            for index in range(len(node.children) - 1, -1, -1):  # reverse children
                queue.put(node.children[index])
        while not yield_stack.empty():
            yield yield_stack.get()

# homework post DFS iterator

if __name__ == '__main__':
    t = Tree(TreeNode('A'))
    t.add_children(t.root, TreeNode('B'), TreeNode('C'), TreeNode('D'))
    node_b = t.find_first('B')
    if node_b != None:
        t.add_children(node_b, TreeNode('H'), TreeNode('I'), TreeNode('J'))
    node_i = t.find_first('I')
    if node_i != None:
        t.add_children(node_i, TreeNode('K'), TreeNode('L'), TreeNode('M'))

    node_c = t.find_first('C')
    if node_c != None:
        t.add_children(node_c, TreeNode('E'), TreeNode('F'), TreeNode('G'))
    print(f'Tree:{t}, of size:{t.size}')
    for node in t.nodes_dfs_preorder():
        print(node.data, end=', ')
    print()
    for node in t.nodes_bfs_preorder():
        print(node.data, end=', ')
    print()
    for node in t.nodes_bfs_postorder():
        print(node.data, end=', ')
