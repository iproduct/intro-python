import sys

cache = {0: 1, 1: 1}

def fib_rec(n: int) -> int:
    if n in cache:
        return cache[n]
    fib_n = fib_rec(n - 1) + fib_rec(n - 2)
    cache[n] = fib_n
    return fib_n

if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    sys.set_int_max_str_digits(10000)
    # for n in range(0, 2000):
    print(fib_rec(2000), end= ', ')