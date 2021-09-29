def some_fun(x, y, nam, *other, name = 'Anonimous', **b):
    for i in range(len(other)):
        print(f'other[{i}] = {other[i]}')
    print(b)
    print(b.items())
    for key, val in b.items():
        print(f'b[{key}] -> {val}')
    print(f'nam = {nam}')
    print(f'name = {name}')


if __name__ == '__main__':
    some_fun(1, 2, 3, 4, name2="Digits", age=25, qualification='programmer')
