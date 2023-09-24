from logged_decorator import logged


# @logged
def fib_gen(number):
    a, b = 0, 1
    for i in range(number):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for f in fib_gen(13):
        print(f, end=', ')