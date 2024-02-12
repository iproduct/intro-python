if __name__ == '__main__':
    s = set(range(1, 11, 2))
    print(s)
    s.add(12)
    s2 = set('Hello from Python!')
    print(s2)

    print(all(x % 2 == 1 for x in s))
    print(any(x % 2 == 0 for x in s))


