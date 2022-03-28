def fibonacci(n):
    a = 0
    b = 1
    while n > 0:
        yield a
        a, b = b, a + b
        n -= 1

if __name__ == '__main__':
    for f in fibonacci(100):
        print(f)

