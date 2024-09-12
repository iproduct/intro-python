from abc import ABC, abstractmethod


class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt
    def __repr__(self):
        return f'({self.data}, {id(self.nxt) if self.nxt is not None else None})'

class Stack(ABC):
    @abstractmethod
    def push(self, node):
        pass
    @abstractmethod
    def pop(self):
        pass
    @abstractmethod
    def peek(self):
        pass
    @abstractmethod
    def is_empty(self):
        pass

class StackLinkedList(Stack):
    def __init__(self):
        self.top = None
    def push(self, data):
        node = Node(data, self.top)
        self.top = node
    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
    def __repr__(self):
        l = []
        head = self.top
        while head is not None:
            l.append(str(head))
            head = head.next
        return '|'.join(l)


if __name__ == '__main__':
    stack = StackLinkedList()
    for i in range(1, 11):
        stack.push(i)
        print(stack)
    while not stack.is_empty():
        print(stack.pop())
        print(stack)