
def f(s: list[str])-> None:
    s[0] = 'x'


if __name__ == '__main__':
    l = list('abcd')
    f(l)
    print(l)