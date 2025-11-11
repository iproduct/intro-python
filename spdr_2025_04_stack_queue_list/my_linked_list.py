from typing import Iterator, Iterable


class Node[T]:
    def __init__(self, data: T, prev: 'Node[T]' = None, nxt: 'Node[T]' = None):
        self.data = data
        self.nxt = nxt
        self.prev = prev
    def __repr__(self):
        return str(self.data)


class LinkedList[T]:
    def __init__(self, values: Iterable[T] = None):
        self.front = None
        self.back = None
        self.size = 0
        if values is not None:
            for value in values:
                self.append(value)

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

    def __getitem__(self, index: int) -> T:
        if index < 0 or index >= self.size:
            raise IndexError(f'Index {index} out of range')
        i = 0
        for val in self.__iter__():
            if i == index:
                return val
            i += 1

    def __setitem__(self, index: int, val):
        self._get_node(index).data = val

    def _get_node(self, index: int) -> Node[T]:
        if index < 0 or index >= self.size:
            raise IndexError(f'Index {index} out of range')
        i = 0
        for node in self._iter_nodes():
            if i == index:
                return node
            i += 1

    def append(self, data: T) -> 'LinkedList[T]':
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

    def prepend(self, data: T) -> 'LinkedList[T]':
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

    def insert(self, index: int, val: T) -> 'LinkedList[T]':
        if index < 0 or index > self.size:
            raise IndexError(f'Index {index} out of range')
        if index == 0:
            self.prepend(val)
        elif index == self.size:
            self.append(val)
        else:
            node = self._get_node(index)
            prev_node = node.prev
            inserted = Node(val, prev_node, node)
            prev_node.nxt = inserted
            node.prev = inserted
        self.size += 1

def reverse(ll: 'LinkedList[T]') -> 'LinkedList[T]':
    result_list = LinkedList()
    for val in ll:
        result_list.prepend(val)
    return result_list

if __name__ == '__main__':
    ll = LinkedList(['a', 'c', 'd', 'e', 'f'])
    # ll.append('a').prepend('b').prepend('c').prepend('d').prepend('e').prepend('f')
    for elem in ll:
        print(elem, end=', ')
    print(f'\nll[3] = {ll[2]}')
    ll.insert(5,'42')
    print(ll)
    print(reverse(ll))