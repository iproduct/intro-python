def fib_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield(a)
        a, b = b, a + b

if __name__ == '__main__':
    fg = fib_gen(3)
    print('before 1', next(fg))
    print('before 2', next(fg))
    print('before 3', next(fg))
    print('before 4', next(fg))
    for f in fg:
        print(f)
    for f in fib_gen(10):
        print(f)



