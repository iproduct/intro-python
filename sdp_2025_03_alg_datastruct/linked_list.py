from typing import Iterator


class Node[T]:
    def __init__(self, data: T, prev: 'Node[T]' = None, nxt: 'Node[T]' = None):
        self.data = data
        self.prev = prev
        self.next = nxt

    def __str__(self):
        return str(self.data)


class LinkedList[T]:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __index__(self, n: int) -> T:
        if n < 0 or n >= self.size:
            raise IndexError('list index out of range')
        return self.__get_node_by_index(n).data

    def __getitem__(self, n: int) -> T:
        return self.__index__(n)

    def __setitem__(self, n, data):
        if n < 0 or n >= self.size:
            raise IndexError('list index out of range')
        self.__get_node_by_index(n).data = data

    def __reversed__(self):
        current = self.tail
        while current is not None:
            yield current.data
            current = current.prev

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '[' + ', '.join(map(str, self)) + ']'

    def __iter_nodes(self) -> Iterator[Node[T]]:
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __get_node_by_index(self, index: int) -> Node[T]:
        if index < 0 or index >= self.size:
            raise IndexError('list index out of range')
        n = 0
        for node in self.__iter_nodes():
            if n == index:
                return node
            n += 1

    def append(self, data: T) -> 'LinkedList[T]':
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            prev_tail = self.tail
            self.tail.next = node
            self.tail = node
            self.size += 1
            node.prev = prev_tail
        return self

    def prepend(self, data: T) -> 'LinkedList[T]':
        node = Node(data)
        if self.tail is None:
            self.tail = node
            self.head = node
            self.size += 1
        else:
            prev_head = self.head
            self.head.prev = node
            self.head = node
            self.size += 1
            node.next = prev_head
        return self

    def pop(self, index: int = None) -> T:
        if index is None:
            index = self.size - 1
        node = self.__get_node_by_index(index)
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1
        return node.data

    def popleft(self) -> T:
        if self.head is None:
            return None
        first = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return first.data

    def insert(self, n: int, data: T) -> 'LinkedList[T]':
        if n < 0 or n > self.size:
            raise IndexError('list index out of range')
        index = 0
        found = None
        for node in self.__iter_nodes():
            if index == n:
                found = node
                break
            index += 1
        if found is None:
            self.append(data)
        else:
            prev_node = found.prev
            if prev_node is None:
                self.prepend(data)
            else:
                node = Node(data, prev_node, found)
                prev_node.next = node
                found.prev = node
                self.size += 1
        return self


if __name__ == '__main__':
    ll: LinkedList[int] = LinkedList()
    ll.append(1).append(2).append(3).append(4).append(5)
    print(ll)
    sentence = 'The Python is easy to learn'
    words = sentence.split(' ')
    words_list: LinkedList[str] = LinkedList()
    for word in words:
        words_list.append(word)
    print(words_list)
    words_list.pop(0)
    print(words_list)
    words_list.append('End')
    words_list.pop()
    words_list.pop(len(words_list) - 1)
    words_list.pop(2)
    print(words_list)
    # words_list.pop(len(words_list))
    while (len(words_list) > 0):
        print(words_list.pop(0))
    # print(words_list.pop(0))
