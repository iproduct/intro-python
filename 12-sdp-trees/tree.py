from abstract_tree import AbstractTree
from queue import LifoQueue, Queue

class TreeNode:
    def __init__(self, data=None, parent=None, children=()):
        self.data = data
        self.parent = parent
        self.children = list(children)

    def __str__(self):
        result = str(self.data)
        if self.children is not None and len(self.children) > 0:
            i = 0
            result += '('
            for child in self.children:
                result += str(child) + (', ' if i < len(self.children) - 1 else '')
                i += 1
            result += ')'
        return result

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def add_children(self, *children):
        for child in children:
            self.add_child(child)

class Tree(AbstractTree):
   def __init__(self, root = None):
       if root is None:
           self.__root = TreeNode()
       else:
           self.__root = root
       self.__size = 0

   def __str__(self):
       return f'({str(self.root())})'

   def size(self):
       return self.__size

   def isEmpty(self):
       return self.__size == 0

   def values_dfs_preorder(self):
       for node in self.nodes_dfs_preorder():
           yield node.data

   #homework: implmenent value iterators for BFS pre- and post-order, and DFS post-order

   def nodes_dfs_preorder(self):
       stack = LifoQueue()
       if root == None: return
       stack.put(self.root())

       while not stack.empty():
           node = stack.get()
           # pre-visit strategy
           yield node
           for child in reversed(node.children):
               stack.put(child)

   def nodes_dfs_postorder(self):
       stack = LifoQueue()
       yields_stack = LifoQueue()
       if root == None: return
       stack.put(self.root())

       while not stack.empty():
           node = stack.get()
           # post-visit strategy
           yields_stack.put(node)
           for child in node.children:
               stack.put(child)
       while not yields_stack.empty():
           yield yields_stack.get();

   def nodes_bfs_preorder(self):
       queue = Queue()
       if root == None: return
       queue.put(self.root())

       while not queue.empty():
           node = queue.get()
           # pre-visit strategy
           yield node
           for child in node.children:
               queue.put(child)

   def root(self):
       return self.__root

   def parent(self, value):
       node = self.find(value)
       return node.parent

   def children(self, value):
       node = self.find(value)
       return node.children

   def isInternal(self, value):
       node = self.find(value)
       return node.children is not None and len(node.children)  > 0

   def isExternal(self, value):
       node = self.find(value)
       return node.children is None or len(node.children)  == 0

   def isRoot(self, value):
       node = self.find(value)
       return node.parent == self.__root

   def swapElements(self, p, q):
       node_p = self.find(p)
       node_q = self.find(q)
       node_p.data, node_q.data = node_q.data, node_p.data

   def replaceElement(self, p, o):
       node_p = self.find(p)
       node_p.data = o

   def find(self, value):
       predicate = lambda node: node.data ==  value
       return self.find_by_predicate(predicate, self.root())

   def find_by_predicate(self, predicate, root = None):
       #recursion bottom
       if root == None:
           return None
       else:
           if root.children is None or len(root.children)  == 0:
              return root if predicate(root) else None

       #pre-visit strategy
       if predicate(root):
           return root
       #recursion step
       for child in root.children:
           result = self.find_by_predicate(predicate, child)
           if result is not None:
               return result

if __name__ == '__main__':
    t = Tree(TreeNode('A'))
    root = t.root()
    root.children.append(TreeNode('B', root, []))
    root.children.append(TreeNode('C', root, []))
    t.find('B').add_children(TreeNode('D'), TreeNode('E'), TreeNode('F'))
    t.find('C').add_children(TreeNode('G'), TreeNode('H'))
    t.find('D').add_children(TreeNode('X'), TreeNode('Y'))
    # print(t)
    # print (str(t.find('B')))
    # print(str(t.find('C')))
    # print(str(t.find('H')))

    print('!!!----- DFS -------!!!')
    for node in t.values_dfs_preorder():
        print(node)

    print('\n!!!----- BFS -------!!!')
    for node in t.nodes_bfs_preorder():
        print(node)
