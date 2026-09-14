# from queue import PriorityQueue
from heap_array import MinHeapArray

if __name__ == '__main__':
    q = MinHeapArray()
    q.insert((2, 'code'))
    q.insert((1, 'eat'))
    q.insert((3, 'sleep'))
    while not q.is_empty():
        next_item = q.extract()
        print(next_item)
        # Резултат:
        # (1, 'eat')
        # (2, 'code')
        # (3, 'sleep')
        