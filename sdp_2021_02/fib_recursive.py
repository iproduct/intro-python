
def fib_recursive(n, cache = {0: 1, 1: 1, 2: 2}):
    if n in cache:
        return cache[n]
    else:
        fib_n = fib_recursive(n-1, cache) + fib_recursive(n-2, cache)
        cache[n] = fib_n
        return fib_n

if __name__ == '__main__':
    for i in range(1, 1000):
        print(f'fib({i}) = {fib_recursive(i)}')