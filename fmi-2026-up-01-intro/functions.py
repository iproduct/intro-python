def f(x):
    x = x + 1
    print('In f() x is: ' , x)
    return x

if __name__ == '__main__':
    x= 3
    f(x)
    print('In main x is: ', x)