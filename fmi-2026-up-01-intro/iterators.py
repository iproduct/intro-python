
if __name__ == '__main__':
    l = ['Hello', 'Python', 'world', '!']
    iterator = iter(l)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    iterator = iter(l)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break