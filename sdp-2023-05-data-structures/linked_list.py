class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


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
            raise IndexError(f'Invalid index = {index}, should be between 0 and {self.length}')
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

    def _nth_node(self, n):
        i = 0
        node = self.first
        while i < n and node is not None:
            node = node.next
            i += 1
        return node

    def push(self, value):
        self.insert(value, self.length)

    def pop(self, index=None):
        if index is None:
            index = self.length - 1
        if index < 0 or index >= self.length:
            raise IndexError(f'Invalid index = {index}, should be between 0 and {self.length - 1}')
        if index == 0:
            result = self.first.value
            self.first = self.first.next
            if self.first is not None:
                self.first.prev = None
            if self.first is None:
                self.last = None
        elif index == self.length - 1:
            result = self.last.value
            self.last = self.last.prev
            self.last.next = None
            if self.last is None:
                self.first = None
        else:
            node = self._nth_node(index)
            result = node.value
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return result

    def peek(self, index=None):
        if index is None:
            index = self.length - 1
        if index < 0 or index >= self.length:
            raise IndexError(f'Invalid index = {index}, should be between 0 and {self.length - 1}')
        return self._nth_node(index)


if __name__ == "__main__":
    my_list = LinkedList()
    values = [1222, 315, 433, 12, 7, 52, 610, 42, 34, 72, 320, 95]
    for v in values:
        my_list.insert(v,0)

    for e in my_list:
        print(e, end = ', ')
    print()

    for i in range(my_list.length):
        print(my_list.pop(), end = ', ')

