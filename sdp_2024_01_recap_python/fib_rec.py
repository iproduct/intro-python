import sys

fib_cache = {0: 0, 1: 1}

def fib_rec(n):
    # if n == 0 or n == 1: # recursion bottom
    #     return n
    if n-1 in fib_cache:
        f1 = fib_cache[n-1]
    else:
        f1 = fib_rec(n-1)
        fib_cache[n-1] = f1
    if n-2 in fib_cache:
        f2 = fib_cache[n-2]
    else:
        f2 = fib_rec(n-2)
        fib_cache[n - 2] = f2
    return f1 + f2


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    print(fib_rec(2000))