def f(x, /, y, *args, name=None, **kwargs) -> None:
    print(x, y)
    print(args, type(args))
    print(name)
    print(kwargs, type(kwargs))

def reverse(*chars):
    return chars[::-1]


if __name__ == '__main__':
    t = 'abcd'
    f(*t, name='abcd', mode='edit', number=5)

    rev = reverse(*'hello_world')
    print(rev)

    # f= lambda *chars: chars[::-1]
    print((lambda *chars: chars[::-1])(*'hello_world'))