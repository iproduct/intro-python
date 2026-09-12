def fib_gen(n):
    a,b = 1,1
    for i in range(n):
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    for n in fib_gen(100):
        print(n)
    for n in fib_gen(20):
        print(n)