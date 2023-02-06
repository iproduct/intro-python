import sys
# sys.set_int_max_str_digits(0)
sys.setrecursionlimit(11000)
from factoriel import fact_iter

def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)

if __name__ == '__main__':
    n = int(input('N='))
    print(f'{n}! Recursive = {fact_rec(n)}')
    print(f'{n}! Iterative = {fact_iter(n)}')