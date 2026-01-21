def print_fibonacci(n):
    a, b = 0, 1
    for i in range(n + 1):
        print(a)
        a, b = b, a+b


if __name__ == '__main__':
   print_fibonacci(100)