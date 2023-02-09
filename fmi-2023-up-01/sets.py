if __name__ == '__main__':
    a = {1, 3, 5, 7, 9}
    print(all(x % 2 > 0 for x in a))
    print(any(x % 2 == 0 for x in a))