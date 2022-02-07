x = "awesome"

def super_outer():
    x = "super"

    def outer():
        x = "outer"

        def myfunc():
            global x
            x = "fantastic"
            print("In myfunc(): Python is", x)

        myfunc()
        print("In outer(): Python is", x)

    outer()
    print("In super_outer(): Python is", x)

if __name__ == '__main__':
    super_outer()
    print("In main: Python is", x)
