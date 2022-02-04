if __name__ == '__main__':
    x = repr(120.0)
    print(x, type(x))
    n = eval(x)
    print(n, type(n))
    s = "Hello Pyton!"

    for i, ch in enumerate(s):
        print(i, ':', ch)

    i = 0
    while i < len(s):
        print(i, ':', s[i])
        i += 1
