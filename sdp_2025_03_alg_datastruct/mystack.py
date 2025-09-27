from stack import Stack


class Node[T]:
    def __init__(self, data: T, prev: 'Node[T]' = None):
        self.data = data
        self.prev = prev
    def __str__(self):
        return str(self.data)

class StackLL(Stack):
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        new_node = Node(item, self.top)
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.prev
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data



