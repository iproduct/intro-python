import sys

memoize = {0:0, 1:1}
calls = 0

def fib(n):
    global calls
    calls += 1
    # if n==0:
    #     return 0
    # elif n==1:
    #     return 1
    if n in memoize:
        print(f"{n} is already fibonacci")
        return memoize[n]
    else:
        print(f"Calling fib({n - 1})  and fib({n-2})")
        fib_n = fib(n-1) + fib(n-2)
        memoize[n] = fib_n
        print(f'fib({n}) = {fib_n} ')
        return fib_n

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    sys.set_int_max_str_digits(10000)
    n = 10
    print(n, '->', fib(n))
    print(f'Number calls: {calls}')