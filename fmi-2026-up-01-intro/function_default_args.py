
def f(x, l = None):
    if l is None:
        l = []
    l.append(x)
    return l

if __name__ == '__main__':
    print(f(10, [1,2,3,4]))
    l1 = f(10)
    print(l1)
    l2 = f(42)
    print(l2)
