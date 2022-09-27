cache = {0: 0, 1: 1}

def fib(n):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n - 2) + fib(n - 1)
        return cache[n]


if __name__ == '__main__':
    for i in range(10000):
        print(i, '->', fib(i))

