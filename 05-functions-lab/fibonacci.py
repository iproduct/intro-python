
# f[0] = 0
# f[1] = 1
# f[n] = f[n-1] + f[n//2], for n >= 2

def get_from_cache(arg, cache, ):
    if arg in cache:
        return cache[arg]

def f_rec(n: int, cache = None) -> int:
    # print(f"f({n}, {cache})")
    if cache is None:
        cache = {0: 0, 1: 1}
    if n < 2 or n in cache:
        return cache[n]
    n2 = cache.get(n // 2, f_rec(n // 2, cache))
    cache[n2] = n2
    n1 = cache.get(n-1, f_rec(n-1, cache))
    cache[n1] = n1
    cache[n] = n1 + n2
    return n1 + n2

if __name__ == '__main__':
    print(f_rec(800))