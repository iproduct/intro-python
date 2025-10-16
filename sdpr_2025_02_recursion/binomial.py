import sys

cache = {}
def binomial(n, k):
    # print(n, k)
    # recursion bottom
    if n < k:
        raise ValueError("n < k")
    if k == n or k == 0:
        return 1
    if (n, k) in cache:
        return cache[(n, k)]
    #recursion step
    n_over_k =  binomial(n-1, k) + binomial(n-1, k-1)
    cache[(n, k)]= n_over_k
    return n_over_k

if __name__ == '__main__':
    sys.setrecursionlimit(11000)
    sys.set_int_max_str_digits(10000)
    # for i in range(10,10000):
    i = 10000
    print(i , ' -> ', binomial(i, 10))