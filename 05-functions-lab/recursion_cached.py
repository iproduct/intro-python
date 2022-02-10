from functools import cache


# f[0] = 0
# f[1] = 1
# f[n] = f[n-1] + f[n//2], for n >= 2

@cache
def f_rec(n: int) -> int:
    print(f"f({n})")
    if n < 2:
        return n
    # if n < 2 or n in cache:
    #     return cache[n]
    # n2 = cache.get(n // 2, f_rec(n // 2, cache))
    # cache[n2] = n2
    # n1 = cache.get(n-1, f_rec(n // 2, cache))
    # cache[n1] = n1
    # cache[n] = n1 + n2
    return f_rec(n // 2) + f_rec(n - 1)


if __name__ == '__main__':
    print(f_rec(800))
