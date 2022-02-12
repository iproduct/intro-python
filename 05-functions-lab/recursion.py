
# f[0] = 0
# f[1] = 1
# f[n] = f[n-1] + f[n//2], for n >= 2
import sys


def f_rec(n: int, cache = None) -> int:
    # print(f"f({n}, {cache})")
    if cache is None:
        cache = {0: 0, 1: 1}
    if n in cache: # recursion bottom
        return cache[n]
    cache[n] = cache.get(n // 2, f_rec(n // 2, cache)) + cache.get(n-1, f_rec(n-1, cache)) # recursion bottom
    return cache[n]

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    print(f_rec(3000))