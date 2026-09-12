def fib_gen(n: int):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    stack = []
    for fib in fib_gen(10):
        stack.append(fib) # push

    while len(stack) > 0:
        elem = stack.pop() # pop
        print(elem)
