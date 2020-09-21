import time


def fib_iter(n):
    i = 2
    fnm2 = 1
    fnm1 = 1
    while i <= n:
        fnm2, fnm1, i = fnm1, fnm2 + fnm1, i + 1
    return fnm1


fib_cache = {}

def fib_rec(n):
    if n <= 1:
        return 1
    else:
        if (n-2) in fib_cache:
            nm2 = fib_cache[n - 2]
        else:
            nm2 = fib_rec(n-2)

        if (n-1) in fib_cache:
            nm1 = fib_cache[n - 1]
        else:
            nm1 = fib_rec(n-1)

        result = nm1 + nm2;
        fib_cache[n] = result;
        return result;


if __name__ == '__main__':
    start_iter = time.time();  # in milliseconds
    for i in range(10000):
        fib_iter(i)
        # print(i, ' -> ', fib_iter(i))
    end_iter = time.time();

    start_rec = time.time();  # in milliseconds
    for i in range(10000):
        fib_rec(i)
        # print(i, ' -> ', fib_rec(i))
    end_rec = time.time();

    print(f'Iterative: {(end_iter - start_iter)  * 1000} ms')
    print(f'Recursive + caching: {(end_rec - start_rec)  * 1000} ms')

