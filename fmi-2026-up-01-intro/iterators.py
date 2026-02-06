from typing import Generator


def fib_gen(n: int) -> Generator[int, None]:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    l = ['Hello', 'Python', 'world', '!']
    iterator = iter(fib_gen(10))
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    iterator = iter(fib_gen(15))
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    for val in fib_gen(5):
        print(val)