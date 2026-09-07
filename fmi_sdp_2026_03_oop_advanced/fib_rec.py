import sys
from functools import cache, lru_cache

from custom_cache import custom_cache
from selective_cache import selective_cache

sys.setrecursionlimit(100000)

@selective_cache('n')
def fib_rec(n, d):
    if n < 2:
        return n
    return fib_rec(n-1, d) + fib_rec(n-2, d)

if __name__ == '__main__':

    # for i in range(1000):
    print(fib_rec(1000, {1:1, 2:2}))