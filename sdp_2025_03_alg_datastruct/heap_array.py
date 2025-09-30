from typing import Callable, Any

from heap import Heap


class MinHeapArray[T](Heap):
    def __init__(self, key: Callable[[T], Any] = lambda x: x):
        self.key = key
        self.elements = []
        self.locator = {}

    def _get_left(self, index: int) -> int:
        return 2 * index + 1

    def _get_right(self, index: int) -> int:
        return 2 * index + 2

    def _get_parent(self, index: int) -> int:
        return index // 2

    def _heepify(self, index, value) -> int:
        while index > 0:
            parent_index = self._get_parent(index)
            if self.key(self.elements[parent_index]) > self.key(self.elements[index]):
                self.elements[parent_index], self.elements[index] = self.elements[index], self.elements[parent_index]
                self.locator[self.elements[parent_index]] = parent_index
                self.locator[self.elements[index]] = index
                index = parent_index
            else:
                break
        return index

    def insert(self, value: T):
        self.elements.append(value)
        index = len(self.elements) - 1
        self.locator[value] = index
        index = self._heepify(index, value)
        print(f'Inseted {value} at index {index}')

    def update_priority(self, value: T):
        print(f'Updating priority for {value}: {self.elements}, {self.locator}')
        index = self.locator[value]
        if index is not None:
            self._heepify(index, value)

    def extract(self) -> T:
        if self.is_empty():
            return None
        result = self.elements[0]
        self.locator[self.elements[0]] = None
        if len(self.elements) == 1:
            return self.elements.pop()
        self.elements[0] = self.elements.pop()
        self.locator[self.elements[0]] = 0
        i = 0
        while i < len(self.elements):
            left = self._get_left(i)
            right = self._get_right(i)
            largest = i
            if left < len(self.elements) and self.key(self.elements[left]) < self.key(self.elements[largest]):
                largest = left
            if right < len(self.elements) and self.key(self.elements[right]) < self.key(self.elements[largest]):
                largest = right
            if largest != i:
                self.elements[i], self.elements[largest] = self.elements[largest], self.elements[i]
                self.locator[self.elements[i]] = i
                self.locator[self.elements[largest]] = largest
            else:
                break
            i = largest
        return result

    def is_empty(self) -> bool:
        return len(self.elements) == 0

if __name__ == '__main__':
    heap: Heap[int] = MinHeapArray()
    heap.insert(5)
    heap.insert(10)
    heap.insert(2)
    heap.insert(1)
    heap.insert(4)
    heap.insert(42)
    heap.insert(41)
    heap.insert(11)
    heap.insert(3)
    heap.insert(9)

    while not heap.is_empty():
        print(heap.extract())