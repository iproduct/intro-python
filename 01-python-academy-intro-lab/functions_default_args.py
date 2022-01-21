def append1(x, list1=[]):
    list1.append(x)
    return list1


def append2(x, list2=[]):
    return list2 + [x]


if __name__ == "__main__":
    print(append1(1))
    print(append1(2))
    print(append2(1))
    print(append2(2))
