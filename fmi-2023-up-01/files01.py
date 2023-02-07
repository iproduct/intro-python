if __name__ == '__main__':
    f = open('files01.py', 'rt')
    for n, line in enumerate(f):
        print(n + 1, ':', line, end='')
    f.close()