if __name__ == '__main__':
    a, b, n, i = 0, 1, 20, 0
    while i < n:
        i += 1
        print(i, '->', b)
        if i == 15:
            break
        a, b = b, a + b
    else:
        print("Good bye")

