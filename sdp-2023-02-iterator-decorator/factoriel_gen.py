def fact_gen(number):
    n = 1
    for i in range(1, number+1):
        n *= i
        yield n

if __name__ == '__main__':
    for f in fact_gen(10):
        print(f, end=', ')