x = "awesome"

def more_outer():
    x = "more"
    def outer():
        nonlocal x
        x = "outer"
        def myfunc():
            nonlocal x
            x = "fantastic"
            print("In myfunc: Python is " + x)
        myfunc()
        print("In outer: Python is " + x)
    outer()
    print("In more_outer: Python is " + x)

if __name__ == '__main__':
    more_outer()
    print("In main: Python is " + x)
