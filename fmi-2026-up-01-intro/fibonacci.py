def print_fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        print(a)
        a, b = b, a + b


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    gen = fib_gen()
    i = next(gen)
    while i < 1000:
        print(i)
        i = next(gen)
    gen2 = fib_gen()
    print(611 in gen2)