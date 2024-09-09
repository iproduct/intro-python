from abc import ABC, abstractmethod


class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = next

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
        self.top = self.top.nxt
        return data
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None