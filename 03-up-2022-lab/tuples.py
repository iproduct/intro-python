import math


def factors(n: int) -> tuple[int]:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return (i,) + factors(n // i)  # recursion step
        i += 1
    return (n,)  # recursion bottom

def factors2(n: int) -> tuple[int]:
    dividers = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            dividers.append(i)
            n = n // i
        else:
            i += 1
    dividers.append(n)
    return tuple(dividers)

def factors3(n: int) -> tuple[int]:
    dividers = []
    rn = range(2, int(math.sqrt(n)) + 1)
    for i in rn:
        while n % i == 0:
            dividers.append(i)
            n = n // i
    return tuple(dividers)



if __name__ == '__main__':
    # t1 = (1, 2, 3)
    # t2 = t1 + (4, 5)
    # print(t1, t2, id(t1), id(t2))
    #
    # # de-packaging
    # p1 = 2, 3
    # p2 = 7, 2
    # segment = p1, p2
    # (x1, y1), (x2, y2) = segment
    # print(x1, y1, x2, y2)

    # number factoring demo
    l, *other, g = factors(840)
    print(l, other, g, sep=" | ")
    l2, *other2, g2 = factors2(840)
    print(l2, other2, g2, sep=" | ")
    l3, *other3, g3 = factors3(840)
    print(l3, other3, g3, sep=" | ")
    l4, *other4, g4 = factors3(2310)
    print(l4, other4, g4, sep=" | ")
