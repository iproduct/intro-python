from collections import deque

from simple_stack_01 import fib_gen

if __name__ == '__main__':
    d = deque()
    for fib in fib_gen(10):
        d.append(fib)

    while len(d) > 0:
        elem = d.popleft()
        print(elem)