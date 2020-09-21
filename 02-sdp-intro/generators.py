def fib(n):
    a, b = 1, 1
    yield 1
    yield 1
    for i in range(n-2):
        a, b = b, a + b
        yield b

    # while i < n - 2:
    #     a, b, i = b, a + b, i + 1
    #     yield b

for f in fib(10):
    print(f)

print('sum = ', sum(fib(10)))