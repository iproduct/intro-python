from functools import reduce
from math import sqrt

if __name__ == "__main__":
    l = [x * x for x in range(1, 11)]
    print(l)

    def is_prime(n):
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
        return True

    n = 10
    primes= [i for i in range(2, n + 1) if is_prime(i)]
    primes= [i*j for i in range(2, n + 1) for j in range(2, n + 1) ]
    primes= {j: [i*j for i in range(2, n + 1)] for j in range(2, n + 1) }
    print(primes)
    fact = {i : reduce(lambda a, x: a * x, (j for j in range(1, i+1))) for i in range(1, n+1)}
    def is_palindrom(s):
        i = 0
        half = len(s) // 2
        while i < half:
            if s[i] != s[-i-1]:
                return False
            i += 1
        return True

    print(is_palindrom("abcdcba"))
    print(is_palindrom("abcdcab"))
    words = ['abcdcba', 'abcdcab', 'neveroddoreven', 'neverevenorodd']

    palindrom = (words)
    print(list(palindrom))