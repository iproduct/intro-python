if __name__ == "__main__":
    s = {1, 2, 3, 4, 5}
    for e in s:
        print(e)
    # print(s[0]) # Error

    print()

    d = {"x":1, "a":4, "c":9, "y":16, "w":25}
    d["b"] = 32
    for k in d:
        print(k, d[k])

    print()

    t = tuple(s)
    for e in t:
        print(e)
    print(t[0])