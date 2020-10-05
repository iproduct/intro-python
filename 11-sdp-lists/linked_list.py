from list import List

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'[{str(self.data)}]'

class LinkedList(List):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__len = 0

    def insert(self, index, e): # O(n)
        node = Node(e)
        if index == 0:
            self.__head, node.next = node, self.__head
        else:
            current = self.get(index - 1)
            current.next, node.next  = node, current.next
        if index == self.count():
            self.__last = node
        self.__len += 1

    def append(self, e): # O(1)
        node = Node(e)
        if self.__last is not None:
            self.__last.next = node
        else:
            self.__head = node
        self.__last = node
        self.__len += 1

    def remove(self, index): # O(n)
        if index < 0 or index > self.count() - 1:
            raise IndexError(f'Index \'{index}\' out of bounds [0, {self.count() - 1}]')
        if index == 0:
            removed = self.__head
            self.__head =  self.__head.next
        else:
            current = self.get(index - 1)
            removed = current.next
            current.next = current.next.next
        if index == self.count() - 1:
            self.__last = current
        self.__len -= 1
        return removed

    def pop(self): # O(n)
        return self.remove(self.count() - 1)

    def get(self, index): # O(n)
        current = self.__head
        i = index
        while i > 0 and not current is None:
            current = current.next
            i -= 1
        if i > 0 or current is None:
            raise IndexError(f'Index \'{index}\' out of bounds [0, {self.count() - 1}]')
        return current

    def slice(self, start, end):
        current = self.get(start)
        slice = LinkedList()
        i = start
        while i < end and current is not None:
            slice.append(current.data)
            current = current.next
            i += 1
        return slice

    def reverse(self):
        current = self.__head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.__last = self.__head
        self.__head = previous

    def count(self):
        return self.__len

    def empty(self):
        return self.__len == 0

    def __str__(self):
        result = ''
        current = self.__head
        while not current is None:
            result += str(current) + ', '
            current = current.next
        return result

    def __len__(self):
        return self.count()

    def insert_sorted(self, e):
        node = Node(e)
        if self.__head is None or e < self.__head.data :
            self.__head, node.next = node, self.__head
            if self.__last == None:
                self.__last = node
        else:
            current = self.__head.next
            previous = self.__head
            while current is not None and current.data < e:
                current, previous = current.next, current
            previous.next, node.next = node, previous.next
            if previous == self.__last:
                self.__last = node
        self.__len += 1

if __name__ == '__main__':
    l = LinkedList()
    l.insert_sorted('one')
    l.insert_sorted('two')
    l.insert_sorted('three')
    l.insert_sorted('four')
    l.insert_sorted('five')
    l.insert_sorted('six')
    # l.remove(4)
    # l.remove(4)
    l.insert_sorted('seven')
    # print(f'Removed: {l.remove(0)}')
    # print(l)
    # print(l.slice(2, 5))
    # print()
    # for i in range(4):
    #     print(l.pop())
    print(l)
    # l.reverse()
    # print(f'Reversed: {l}')
