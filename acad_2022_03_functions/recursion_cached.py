import sys
from functools import lru_cache


# f[0] = 0
# f[1] = 1
# f[n] = f[n-1] + f[n//2], for n >= 2

@lru_cache(100)
def f_rec(n: int) -> int:
    # print(f"f({n})")
    if n < 2:
        return n
    return f_rec(n // 2) + f_rec(n - 1)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    print(f_rec(1000))
