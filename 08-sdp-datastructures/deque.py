from collections import deque

if __name__ == '__main__':
    print('Stack Demo:')
    stack = deque()
    stack.append('one')
    stack.append('two')
    stack.append('three')
    stack.append('four')
    stack.append('five')
    stack.append('six')

    while len(stack) > 0:
        print(stack.pop())

    print('\nQueue Demo:')
    queue = deque()
    queue.appendleft('one')
    queue.appendleft('two')
    queue.appendleft('three')
    queue.appendleft('four')
    queue.appendleft('five')
    queue.appendleft('six')

    while len(queue) > 0:
        print(queue.pop())