
def print_fib(n: int):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a + b

if __name__ == '__main__':
    print_fib(100)

