def func(a, b, /, c, d = 100, *names, e = 'hi', f, **kwargs):
    print(a, b, c, d, e, f)
    print('args=', names)
    print('kwargs=', kwargs)

if __name__ == '__main__':
    func(1, 2, 3, 4, 5, 6, 7, 8, 9, f = 42, g = 18, h = 72, w = 'Hello')