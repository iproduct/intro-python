cache = {0:0, 1:1}
def fib(n):
    if n == 0 or n == 1:
        return n
    # print(n, ": ", cache)
    if n-2 in cache:
        fn2 = cache[n-2]
    else:
        fn2 = fib(n - 2)
    if n-1 in cache:
        fn1 = cache[n-1]
    else:
        fn1 = fib(n - 1)
    result =  fn2 + fn1
    cache[n] = result
    return result

if __name__ == '__main__':
    # for n in range(10):
    #     print(n, ' -> ', fib(n))
    print(fib(100))