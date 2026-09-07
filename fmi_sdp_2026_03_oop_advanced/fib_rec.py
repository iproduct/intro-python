import sys
from functools import cache, lru_cache

from custom_cache import custom_cache

sys.setrecursionlimit(100000)

@custom_cache
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

if __name__ == '__main__':

    # for i in range(1000):
    print(fib_rec(999))