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
        self.front = None
        self.back = None
        self.size = 0

    def __len__(self):
        return self.size

    def _iter_nodes(self) -> Iterator[Node[T]]:
        current = self.front
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
            if node != self.back:
                result += ', '
        result += ']'
        return result

    def append(self, data: T) -> Node[T]:
        node = Node(data)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.nxt = node
            node.prev = self.back
            self.back = node
        self.size += 1
        return self

    def prepend(self, data: T) -> Node[T]:
        node = Node(data)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.front.prev = node
            node.nxt = self.front
            self.front = node
        self.size += 1
        return self

if __name__ == '__main__':
    ll = LinkedList()
    ll.append('a').prepend('b').prepend('c').prepend('d').prepend('e').prepend('f')
    for elem in ll:
        print(elem, end=', ')