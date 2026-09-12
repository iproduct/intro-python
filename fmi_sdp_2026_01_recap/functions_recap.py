

def main():
    def f(y):
        nonlocal x
        x = 42
        y[0] = 42
    x = 5
    y = [1, 2, 3, 4, 5]
    print(f(y))
    print(x, y)

if __name__ == '__main__':
    main()