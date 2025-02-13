def f(x, y, /, z, *args, mode='read', **kwargs):
    print(x, y, z, args, mode, kwargs)

def wrapper(*args, **kwargs):
   f(*args, **kwargs)

def fx(y):
    # x = 1
    print(x)
    print(x+1)
    if True:
        z = 4
    print(z)

x = 5

if __name__ == '__main__':
    f(1, 2, 3,  4, 5, 6, mode='write', color='red', highlight='green')
    f(1, 2, z=3)
    fx(0)
    print('x = ', x)