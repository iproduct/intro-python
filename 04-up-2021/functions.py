
def f(x, y):
    global g
    g = 3
    x = 2
    y[0] = 'hi'
    print("inside f - g:", g)

def ft(x, y):
    x = 2
    return ('hi', y[1], y[2])

g = 42

if __name__ == "__main__":
    a = 12 #immutable
    l = ['a', 'b', 'c'] # mutable
    f(a, l)
    print(a)
    print("List (mutable):", l)

    t = ('a', 'b', 'c') # immutable
    z = ft(a, t)
    print("Tuple (immutable):", z)

    print("Global g:", g)