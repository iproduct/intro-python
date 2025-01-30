import sys
sys.setrecursionlimit(1500)

def fact_iter(n: int) -> int:
    """
    Calculates the factorial of n
        :param n: number to compute factorial for
        :return: the n!
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fact_rec(n: int) -> int:
    """
    Calculates the factorial of n
        :param n: number to compute factorial for
        :return: the n!
    """
    if n <= 1:  # recursion bottom
        return 1
    else:      # recursion step
        return n * fact_rec(n - 1)


if __name__ == '__main__':
    # for n in range(1, 21):
    #     fact_n = fact_rec(n)

    print(f'Iterative 1000! = {fact_iter(1000)}')
    # n = 8
    # print(f'{n}! = {fact_rec(n)}')
