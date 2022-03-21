g = 42
def outer():  # closure = enclosing scope
    g = 1024
    def middle():
        g1 = 255
        def inner():
            nonlocal g
            g = 108
            print("In inner:", g)
        inner()
        print("In middle:", g)
    middle()
    print("In outer:", g)

if __name__ == '__main__':
    outer()
    print("In main:", g)
