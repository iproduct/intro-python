from mystack import StackLL
from stack import Stack


def fib_gen(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    stack: Stack = StackLL()
    for fib in fib_gen(10):
        stack.push(fib) # push

    while not stack.is_empty():
        elem = stack.pop() # pop
        print(elem)
