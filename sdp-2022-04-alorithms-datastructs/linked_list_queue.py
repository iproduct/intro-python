class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return self.value


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node.value
            node = node.next


    def enqueue(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, None, self.first)
            self.first.prev = new_node
            self.first = new_node

    def dequeue(self):
        if self.last is None:
            return None
        else:
            result = self.last.value
            self.last = self.last.prev
            if self.last is None:
                self.first = None
            return result

    def peek(self):
        return None if self.last is None else self.last.value

    def empty(self):
        return self.last is None

    def __str__(self):
        result = '['
        node = self.last
        while node is not None:
            result += str(node.value) + (', ' if node.prev is not None else '')
            node = node.prev
        result += ']'
        return result

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(12)
    queue.enqueue(43)
    queue.enqueue(7)
    queue.enqueue(115)
    queue.enqueue(42)
    queue.enqueue(79)
    print(queue)
    while not queue.empty():
        print(queue.dequeue())