import sys
from itertools import permutations
from typing import Iterator

from logged_decorator import logged
from profile_decorator import profile

sys.setrecursionlimit(100000)

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



# @logged(print_args=False)
@profile
def test_get_perm(s):
    results = []
    for p in get_perm(s):
        results.append(''.join(p))

if __name__ == '__main__':
    test_get_perm(tuple([chr(l) for l in range(65,75)]))
    # for p in str_perm_gen('abcde'):
    #     print(p, end=', ')
