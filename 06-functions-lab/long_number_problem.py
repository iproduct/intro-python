

def find_index(pred, sequence, start = 0):
    # for index in range(start, len(iterable)):
    i = start
    length = len(sequence)
    while i < length:
        if pred(sequence[i]):
            return i
        i += 1

if __name__ == '__main__':
    # n = int(input("Number length:"))
    s = input("Number:")
    f_map = input("Mapping function:").split()
    f = lambda c: f_map[int(c) - 1]
    print([f(x) for x in range(1,10)])
    start = find_index(lambda c: f(c) > c, s, 0)
    if start is None:
        start = len(s)
    end = find_index(lambda c: f(c) < c, s, start + 1)
    if end is None:
        end = len(s)
    print(start, end, s[start : end])

    result = s[:start] + "".join(list(map(f, s[start : end]))) + s[end: ]
    print(result)


