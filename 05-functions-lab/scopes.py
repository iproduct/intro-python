
x = 42


def closure(): # closure == enclosing scope
    x = 105
    def f(): # local scope
        nonlocal x
        x = 15 # shadowing
        print("In f() x = ", x)
    f()
    print("In closure() x = ", x)

if __name__ == '__main__':
    closure()
    print("In main script x = ", x)