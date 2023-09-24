from itertools import permutations
from typing import Iterator

from logged_decorator import logged


def str_perm_gen(s: str) -> Iterator[str]:
    for letters in permutations(s):
        yield ''.join(letters)

@logged
def get_perm(tuple):
    n = len(tuple)
    if n <= 1:                  # recursion bottom
        yield tuple
    else:
        for rest in get_perm(tuple[1:]):    # recursion step
            for i in range(n):
                perm = rest[:i] + (tuple[0],) + rest[i:]
                yield perm


if __name__ == '__main__':
    for p in get_perm(tuple('abcde')):
        print(''.join(p), end=', ')
    print()
    for p in str_perm_gen('abcde'):
        print(p, end=', ')
