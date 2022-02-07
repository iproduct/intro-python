import math


def factor_r1(n: int, factors = None) -> list[int]:
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
        factors.append(n) # recursion bottom
    return factors


def factor_r2(n: int) -> list[int]:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return [i] + (factor_r2(n // i))  # recursion step
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


if __name__ == '__main__':
    n = 840
    factors = []
    print(factor_r1(n))
    print(factor_r1(n, factors))
    print("Factors:", factors)
    # print(factor_r2(n, factors))
    # print(factors)
    print(factor_i1(n))
    print(n)
