def f(x, y, /, z, *args, mode='read', **kwargs):
    print(x, y, z, args, mode, kwargs)


if __name__ == '__main__':
    f(1, 2, z=3, 4, 5, 6, mode='write', color='red', highlight='green')
    f(1, 2, z=3)
