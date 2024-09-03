def fib_gen(n):
    a, b, i = 1, 1, 0
    while i < n:
        yield a
        i += 1
        a, b = b, a + b


if __name__ == '__main__':
    for f in fib_gen(10):
        print(f)