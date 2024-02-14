def f(x, y= 15, /, a = 42, *args , separator = ' ', end='\n', **kwargs):
    suffix = kwargs.get('suffix', '!!!')
    print(kwargs['prefix'], x, y, a, args, kwargs, suffix, sep=separator, end=end)

if __name__ == "__main__":
    f(7, 8, 9, 10, 11, 12,13,separator='|', end="\n\n", prefix='In f():')
    f(12,13,14,15, 16, suffix='!', prefix='In f():')