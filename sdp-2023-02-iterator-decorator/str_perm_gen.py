from itertools import permutations
from typing import Iterator


def str_perm_gen(s: str) -> Iterator[str]:
    for letters in permutations(s):
        yield ''.join(letters)

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
    for p in get_perm(tuple('abcd')):
        print(''.join(p), end=', ')
    print()
    for p in str_perm_gen('abcd'):
        print(p, end=', ')
