
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

