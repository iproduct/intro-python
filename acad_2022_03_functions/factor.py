import math
import sys

from profile_decorator import profile


def factor_r1(n: int, factors=None) -> list[int]:
    if factors is None:
        factors = []
    i = 2
    limit = int(math.sqrt(n))
    while i <= limit:
        if n % i == 0:
            factors.append(i)
            factor_r1(n // i, factors)  # recursion step
            break
        i += 1
    else:
        factors.append(n)  # recursion bottom
    return factors


def factor_r2(n: int) -> list[int]:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return [i] + (factor_r2(n // i))  # recursion step
    return [n]  # recursion bottom


def factor_r3(n: int) -> list[int]:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return [i] + (factor_r3(n // i))  # recursion step
        i += 1
    return [n]  # recursion bottom


def factor_i1(n: int) -> list[int]:
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    factors.append(n)
    return factors


@profile
def test(func, *args, count=1000, **kwargs):
    while count:
        func(*args, **kwargs)
        count -= 1


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)
    n = 1000000
    iterations = 100000
    factors = []
    test(factor_r1, n, count=iterations)
    # print(factor_r1(n, factors))
    # print("Factors:", factors)
    test(factor_r2, n, count=iterations)
    test(factor_r3, n, count=iterations)
    test(factor_i1, n, count=iterations)
