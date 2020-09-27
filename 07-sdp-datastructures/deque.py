from collections import deque

if __name__ == '__main__':
    stack = deque()
    stack.append('one')
    stack.append('two')
    stack.append('three')
    stack.append('four')
    stack.append('five')
    stack.append('six')

    while len(stack) > 0:
        print(stack.pop())