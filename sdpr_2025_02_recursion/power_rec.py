import sys

def power(base, exponent):
    #recursion bottom
    if exponent == 0:
        return 1
    # recursion step
    return power(base, exponent - 1) * base

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    sys.set_int_max_str_digits(10000)
    x = 2
    n = 10
    print(f'{x}**{n} = {power(x, n)}')