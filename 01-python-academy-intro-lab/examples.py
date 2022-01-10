
"""Python intro examples"""

def square(x):
    """Squares the argument"""
    print(__name__)
    return x * x

if __name__ == "__main__":
    m = map(square, range(1,5))
    m2 = map(square, range(1,5))

    for item in m:
        print(item)

    print(list(m2))

    print([it * it for it in map(square, range(1,5)) if it % 2 == 0])

    print(tuple(it * it for it in map(square, range(1, 5)) if it % 2 == 0))

    print({it * it for it in map(square, range(1, 5)) if it % 2 == 0})

    d = {it: it * it for it in map(square, range(1, 5)) if it % 2 == 0}

    lkv = list(d.items())
    print (lkv)
    print(list(d.keys()))
    print(list(d.values()))

    print(*(e for e in lkv))