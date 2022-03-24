def find_first_index(predicate, str_, start=0):
    i = start
    length = len(str_)
    while i < length:
        if predicate(str_[i]):
            return i
        i += 1
    return length


def find_substitution(n: int, number: str, f_map: str) -> tuple[int, int, str]:
    fmlist = f_map.split(' ')
    f = lambda digit: fmlist[int(digit) - 1]
    start = find_first_index(lambda c: f(c) > c, number)
    end = find_first_index(lambda c: f(c) < c, number, start + 1)
    result = number[:start] + "".join(map(f, number[start:end])) + number[end:]
    return start, end, result
