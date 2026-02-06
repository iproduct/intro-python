import sys
from typing import Dict

fib_cache: Dict[int, int] = {0:0, 1:1}

def fib_rec(n: int) -> int:
    if n in fib_cache:
        return fib_cache[n]
    fib_n = fib_rec(n - 1) + fib_rec(n - 2)
    fib_cache[n] = fib_n
    return fib_n


if __name__ == '__main__':
    sys.set_int_max_str_digits(100000)
    for i in range(100000):
        print(i, ' -> ', fib_rec(i))
