
# python generator function
def fib(max):
    """Връща като списък първите n числа на Фибоначи"""
    result = []
    a, b = 0, 1
    n = 0
    while n < max:
         yield a
         a, b = b, a+b
         n += 1

if __name__=="__main__":
    # 1 - using next()
    f = fib(10)
    print("\nUsing next:")
    finished = False
    while not finished:
        try:
            x = next(f)
            print(x)
        except StopIteration:
            finished = True
            print('End of program')

    # 2 - using for
    print("\nUsing for:")
    for x in fib(10):
        print(x)
    else:
        print('End of program')