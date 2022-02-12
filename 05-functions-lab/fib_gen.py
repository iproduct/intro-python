from typing import Iterator


def fib_gen(count: int = 10) -> Iterator[int]:
    a = 0
    b = 1
    yield a
    while count:
        yield b
        a, b = b, a + b
        count -= 1

if __name__ == "__main__":
    print("Using while:")
    fg_instance = iter(fib_gen(20))
    try:
        while True:
            print(next(fg_instance))
    except StopIteration:
        pass
    print("Using for:")
    for i, fib in enumerate(fib_gen(20)):
        print(i, ":", fib)
    print("Demo end.")