
def find_first_index(predicate, sequence, start=0):
    """
    Find index of first element in sequence that satisfies the given predicate
    :param predicate: boolean function of sequence element
    :param sequence: sequence of elements
    :param start: start of the search index
    :return: the first index of element that satisfies the predicate
    """
    i = start
    len_ = len(sequence)
    while i < len_:
        if predicate(sequence[i]):
            return i
        i += 1


if __name__ == '__main__':
    s = input("Enter number:").strip()
    n = len(s)
    f_map = input("Mapping function:").split()
    print(f"number: {s}, mapping: {f_map}")
    start = find_first_index(lambda digit: f_map[int(digit) - 1] > digit , s, 0)
    if start is None:
        start = len(s)
    end = find_first_index(lambda digit: f_map[int(digit) - 1] < digit, s, start)
    if end is None:
        end = len(s)
    print(f"start: {start}, end: {end}")
    result = s[:start] + "".join(list(map(lambda digit: f_map[int(digit) - 1], s[start: end]))) + s[end:]
    print(result)

