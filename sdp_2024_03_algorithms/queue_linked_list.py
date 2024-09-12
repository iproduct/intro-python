from abc import ABC, abstractmethod


class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt
    def __repr__(self):
        return f'({self.data}, {id(self.nxt) if self.nxt is not None else None})'

class Queue(ABC):
    @abstractmethod
    def enqueue(self, node):
        pass
    @abstractmethod
    def dequeue(self):
        pass
    @abstractmethod
    def peek(self):
        pass
    @abstractmethod
    def is_empty(self):
        pass


class QueueLinkedList(Queue):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node

    def dequeue(self):
        if self.head is None:
            raise Exception('Queue is empty')
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        if self.head is None:
            raise Exception('Queue is empty')
        return self.head.data

    def is_empty(self):
        return self.head is None

    def __repr__(self):
        l = []
        head = self.head
        while head is not None:
            l.append(str(head))
            head = head.next
        return '|'.join(l)

if __name__ == '__main__':
    q = QueueLinkedList()
    for i in range(26):
        q.enqueue(chr(ord('A') + i))
        print(q)

    while not q.is_empty():
        print(q.dequeue())
