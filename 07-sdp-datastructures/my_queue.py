
class MyQueue:
    def __init__(self, values = []):
        self.__stack = values

    def enqueue(self, value):
        self.__stack.insert(0, value)

    def dequeue(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def __len__(self):
        return len(self.__stack)


class BoundedQueue:
    def __init__(self, size=1024, values = []):
        self.__stack = values[:size]
        self.__stack.extend([None] * (size - len(values)))
        self.__size = size
        self.__first = 0
        self.__last = 0
        self.__len = 0

    def enqueue(self, value):
        if self.__len__() == self.__size:
            raise QueueException('Queue is full. Can not add new element.')
        self.__stack[self.__last] = value
        self.__last = (self.__last + 1) % self.__size
        self.__len += 1
        # print(f'!!!self.__len__, __len={self.__len__()}, {self.__size}')
        # print(f'!!!self.__last={self.__last}')

    def dequeue(self):
        if self.__len__() == 0:
            raise QueueException('Queue is empty. Can not dequeue an element.')
        result = self.__stack[self.__first]
        # print(f'!!!self.__len__, __len={self.__len__()}, {self.__size}')
        # print(f'!!!result, self.__first={result}, {self.__first}')
        self.__first = (self.__first + 1) % self.__size
        self.__len -= 1
        return result

    def peek(self):
        if self.__len__() == 0:
            raise QueueException('Queue is empty. Can not peek an element.')
        return self.__stack[self.__first]

    def __len__(self):
       return self.__len

class QueueException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__== '__main__':
    queue = BoundedQueue(6)
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')
    queue.enqueue('f')

    print (f'Size: {len(queue)}')
    print (f'First: {queue.peek()}')

    while len(queue) > 0:
    # for i in range(8):
        try:
            print(queue.dequeue())
        except QueueException as qe:
            print(f'Error: {qe}')
