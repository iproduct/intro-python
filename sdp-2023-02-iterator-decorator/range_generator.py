def range_gen(start, end, step = 1):
    i = start
    while i < end if step > 0 else i > end:
        yield i
        i += step

if __name__ == '__main__':
    for f in range_gen(20, 0, -3):
        print(f, end=', ')