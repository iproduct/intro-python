import sys
import time


def timed(func):
    def inner(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        end = time.time_ns()
        print(f'Function {func} took: {(end - start) / 1000000} ms')
        return result

    return inner


@timed
def fact_rec(n):
    return 1 if n <= 1 else fact_rec(n - 1) * n


@timed
def fact_iter(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i += 1
    return result


if __name__ == '__main__':
    sys.setrecursionlimit(1100)
    # print(fact_rec(500))
    print(fact_iter(50000))
