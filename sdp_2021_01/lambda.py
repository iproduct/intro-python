L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]  # Списък с 3 анонимни функции

if __name__ == '__main__':
    for f in L:
        print(f(3))
    print(L[2](5))
