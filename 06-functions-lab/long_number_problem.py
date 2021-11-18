

def find_index(pred, iterable, start = 0):
    pass

if __name__ == '__main__':
    # n = int(input("Number length:"))
    s = input("Number:")
    f_map = input("Mapping function:").split()
    f = lambda c: f_map[int(c) - 1]
    print([f(x) for x in range(1,10)])
    bigger_eq_pred = lambda c: f(c) >= c


