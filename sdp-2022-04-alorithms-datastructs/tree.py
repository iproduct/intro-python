
class TreeNode:
    def __init__(self, data = Node, parent= None, children=()):
        self.data = data
        self.parent = parent
        self.children = children

    def __str__(self):
        result = str(self.data)
        if self.children is not None and len(self.children) > 0:
            i = 0
            result += '('
            for child in self.children:
                result += str(child) + (', ' if i < len(self.children) - 1 else '')
                i += 1
            result += ')'
        return  result

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def add_children(self, *children):
        for child in children:
            self.add_child(child)

class Tree(AbstractTree):
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        
    def __str__(self):
        return str(self.root)
    
    def is_empty(self):
        return size == 0

    def size(self):
        return size

    def values_dfs_postorder(self):
        for node in self.nodes_dfs_preorder():
            yield node.data

    def nodes_dfs_preorder(self):
        stack = Stack()
        if root == None: return
        stack.push(self.root)
        while not stack.is_empty():
            node = stack.pop()
            # pre-visit strategy
            yield node
            for child in reversed(node.children):
                stack.push(child)

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