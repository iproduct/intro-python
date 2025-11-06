from typing import Iterator


class Node[T]:
    def __init__(self, data: T, prev: 'Node[T]' = None, nxt: 'Node[T]' = None):
        self.data = data
        self.nxt = nxt
        self.prev = prev
    def __repr__(self):
        return str(self.data)


class LinkedList[T]:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def _iter_nodes(self) -> Iterator[Node[T]]:
        current = self.head
        while current:
            yield current
            current = current.nxt

    def __iter__(self):
       for node in  self._iter_nodes():
           yield node.data

    def __repr__(self):
        result = '['
        for node in self._iter_nodes():
            result += str(node.data)
            if node != self.tail:
                result += ', '
        result += ']'
        return result

    def append(self, data: T) -> Node[T]:
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return self

if __name__ == '__main__':
    ll = LinkedList()
    ll.append('a').append('b').append('c').append('d').append('e').append('f')
    print(ll)