def count_down(value):
    for x in range(value, 0, -1):
        yield x

if __name__ == '__main__':
    gen = count_down(3)
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    # print(gen.__next__())
    for val in count_down(3):
        print(val)

