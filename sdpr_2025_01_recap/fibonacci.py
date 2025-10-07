def print_fib(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    print_fib(30)