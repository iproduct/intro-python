def gen_fib(n):
    a, b, i = 1, 1, 0
    for i in range(n):
        yield (i, a)
        a, b = b, a + b

if __name__ == '__main__':
    for i, val in gen_fib(15):
        print(f'fib({i}) = {val}')

