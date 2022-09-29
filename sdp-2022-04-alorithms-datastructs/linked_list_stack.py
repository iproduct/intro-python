class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


class Stack:
    def __init__(self):
        self.top = None

    def __iter__(self):
        node = self.top
        while node is not None:
            yield node.value
            node = node.next


    def push(self, value):
        if self.top is None:
            self.top = Node(value)
        else:
            new_node = Node(value, self.top)
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            result = self.top.value
            self.top = self.top.next
            return result

    def peek(self):
        return None if self.top is None else self.top.value

    def empty(self):
        return  self.top is None

    def __str__(self):
        result = '['
        node = self.top
        while node is not None:
            result += str(node.value) + (', ' if node.next is not None else '')
            node = node.next
        result += ']'
        return result

if __name__ == '__main__':
    stack = Stack()
    stack.push(12)
    stack.push(43)
    stack.push(7)
    stack.push(115)
    stack.push(42)
    stack.push(79)
    print(stack)
    while not stack.empty():
        print(stack.pop())