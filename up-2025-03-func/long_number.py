from collections.abc import Sequence
from typing import Callable, Iterable

a= '13737'
maping = '1 2 5 4 6 6 3 1 9'
maping_digits = maping.split(' ')

type digit = str

def f(d: digit) -> digit:
    return maping_digits[int(d) - 1]

def find_first(seq: Sequence, pedicate: Callable[[digit], bool], start = 0 ) -> int:
    index = start
    length = len(seq)
    while index < length:
        if pedicate(seq[index]):
            return index
        index += 1
    return index

def main(a: str, f: Callable[[digit], digit]) -> (int, int):
    start = find_first(a, lambda d: f(d) > d)
    end = find_first(a, lambda d: f(d) < d, start)
    return start, end

if __name__ == '__main__':
    start, end = main(a, f)
    result = a[:start] +  ''.join(list(map(f,a[start: end]))) + a[end:]
    print(f'[start, end] -> {result}')