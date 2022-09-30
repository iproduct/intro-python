class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.value
            node = node.next

    def insert(self, value, index=0):
        if index < 0 or index > self.length:
            raise IndexError(f'Invalid index = {index}, should be in [0, {self.length})')
        if index == 0:
            new_node = Node(value, None, self.first)
            if self.first is not None:
                self.first.prev = new_node
            self.first = new_node
            if self.last is None:
                self.last = new_node
        elif index == self.length:
            new_node = Node(value, self.last, None)
            self.last.next = new_node
            self.last = new_node
        else:
            node = self._nth_node(index)
            new_node = Node(value, node.prev, node)
            node.prev.next = new_node
            node.prev = new_node
        self.length += 1

    def append(self, value):
        return self.insert(value, self.length)

    def pop(self, index=None):
        if index is None:
            index = self.length - 1
        if index < 0 or index >= self.length:
            raise IndexError(f'Invalid index = {index}, should be in [0, {self.length})')
        if index == self.length - 1:
            result = self.last.value
            self.last = self.last.prev
            if self.last is not None:
                self.last.next = None
            if self.last is None:
                self.first = None
        elif index == 0:
            result = self.first.value
            self.first = self.first.next
            self.first.prev = None
            if self.first is None:
                self.last = None
        else:
            result = self._nth_node(index)
            result.prev.next = result.next
        self.length -= 1
        return result

    def _nth_node(self, n):
        if n <= self.length // 2:
            i = 0
            node = self.first
            while i < n and node is not None:
                node = node.next
                i += 1
        else:
            i = self.length - 1
            node = self.last
            while i > n and node is not None:
                node = node.prev
                i -= 1
        return node

    def peek(self):
        return None if self.last is None else self.last.value

    def empty(self):
        return self.length == 0

    def __str__(self):
        result = '['
        node = self.first
        while node is not None:
            result += str(node.value) + (', ' if node.next is not None else '')
            node = node.next
        result += ']'
        return result


if __name__ == '__main__':
    mylist = LinkedList()
    values = [12, 43, 7, 115, 42, 79]
    for val in values:
        mylist.insert(val)
    print(mylist)
    mylist.insert(1000, 4)
    print(mylist)
    mylist.pop(6)
    print(mylist)
    while not mylist.empty():
        print(mylist.pop(0), mylist.length)

