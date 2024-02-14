def my_range(start, end, step=1):
    i = start
    while i < end:
        yield i
        i += step


def fib(n=10):
    i = 0
    a, b = 0, 1
    while i < n:
        yield a
        a, b = b, a+b
        i += 1


if __name__ == "__main__":
    for result in my_range(0, 100):
        print(result, end=", ")
    print('\n')
    for result in fib(100):
        print(result, end=", ")
