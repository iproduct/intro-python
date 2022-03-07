from functools import reduce

if __name__ == '__main__':
    l = list(range(10))
    print(l)
    l.append(3)
    l.insert(1, 3)
    l.extend([5,3,7])
    print(l)
    print(l.index(3))
    i = -1
    while True:
        try:
            i = l.index(3, i+1)
            print(i)
        except:
            break
    # s = "".join([str(i) for i in l])
    s = reduce(lambda acc, x: acc + str(x), l, "")
    print(s)
    print(s.find("3"))
    i=0
    while True:
            i = s.find("3", i+1)
            if i < 0:
                break
            print(i)

    print(l[::-1])
    l.reverse()
    print(l)
    sorted = l.copy()
    sorted.sort(reverse=True)
    print(sorted)
    print(l)

