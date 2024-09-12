from collections.abc import Iterable


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev
    def __repr__(self):
        return f'({self.data}, {id(self.prev) if self.prev is not None else None}, {id(self.next) if self.next is not None else None})'


class LinkedList:
    def __init__(self, iterable: Iterable = None):
        self.__first = None
        self.__last = None
        self.__size = 0
        prev = None
        if iterable is not None:
            for it in iterable:
                self.append(it)
                self.__size += 1

    def __iter__(self):
        node = self.__first
        while node is not None:
            yield node.data
            node = node.next

    def reverse(self):
        node = self.__last
        while node is not None:
            yield node.data
            node = node.prev

    def __len__(self):
        return self.__size

    def __getitem__(self, start, stop, step):
        index = start
        if stop == None:
            end = start + 1
        else:
            end = stop
        if step == None:
            stride = 1
        else:
            stride = step

        result = LinkedList()
        if stride > 0:
            i = 0
            for it in self:
                if i % stride == 0:
                    result.append(it)
                if i >= stop:
                    break
                i += 1
        elif stride < 0:
            i = self.__size
            for it in self.reverse:
                if i % stride == 0:
                    result.append(it)
                if i <= stop:
                    break
                i -= 1
        return result

    def __repr__(self):
        node = self.__first
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next
        return f'[{', '.join(result)}]'

    def insert(self, data, index):
        if index < 0 or index > self.__size:
            raise IndexError('Index out of range')

        if self.__first is None: # empty list
            node = Node(data)
            self.__first = node
            self.__last = node
        elif index == 0:
            node = Node(data, None, self.__first)
            self.__first.prev = node
            self.__first = node
        elif index == self.__size:
            node = Node(data, self.__last, None)
            self.__last.next = node
            self.__last = node
        else:
            found = self.__get_nth_node(index)
            node = Node(data, found.prev, found)
            found.prev.next = node
            found.prev = node

        self.__size += 1

    def append(self, data):
        self.insert(data, self.__size)
        print(self)

    def __get_nth_node(self, index):
        if index < 0 or index > self.__size:
            raise IndexError('Index out of range')
        if index < self.__size // 2:
            node = self.__first
            while index > 0 and node.next is not None:
                index -= 1
                node = node.next
        else:
            node = self.__last
            while index < self.__size and node.next is not None:
                index += 1
                node = node.prev
        return node

    def get(self, index):
        return self.__get_nth_node(index).data

    def pop(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError('Index out of range')
        if index == 0:
            node = self.__first
            if node.next is None:
                self.__first = self.__last = None
            else:
                node.next.prev = None
                self.__first = node.next
        elif index == self.__size - 1:
            node = self.__last
            node.prev.next = None
            self.__last = node.prev
        else:
            node = self.__get_nth_node(index)
            node.prev.next = node.next
            node.next.prev = node.prev
        self.__size -= 1
        return node

    def is_empty(self):
        return self.__size == 0

if __name__ == '__main__':
    l = LinkedList()
    print(l)
    for it in range(26):
        l.append(chr(ord('A') + it))
    print(l)