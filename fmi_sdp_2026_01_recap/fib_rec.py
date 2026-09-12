import sys

cache = {}

def fib_rec(n):
    if n <2:
        return n
    if n in cache:
        return cache[n]
    result = fib_rec(n-1) + fib_rec(n-2)
    cache[n] = result
    return result

if __name__ == '__main__':
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    # for i in range(100):
    print(fib_rec(1000))