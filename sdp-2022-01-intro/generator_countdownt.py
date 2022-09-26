def countdown(n):
    for i in range(n, 1, -1):
        yield i
    yield 'Lift Off!'
    yield 'Demo finished.'

if __name__ == '__main__':
    for x in countdown(10):
        print(x)