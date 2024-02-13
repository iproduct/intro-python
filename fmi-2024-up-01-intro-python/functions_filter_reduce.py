import math
import time

if __name__ == '__main__':

    N = 100000
    # A. N//2
    start = time.time_ns()
    result = filter(lambda n: all(n % d != 0 for d in range(2, n // 2 + 1)), range(2, N + 1))
    for n in result:
        pass
    end = time.time_ns()
    print(f'N//2: N={N} -> {(end - start) / 1000000:>12.4f} ms')


    # B. sqrt(N)
    start = time.time_ns()
    result = filter(lambda n: all(n % d != 0 for d in range(2, int(math.sqrt(n)) + 1)), range(2, N + 1))
    for n in result:
        pass
        # print(n, end=' ')
    end = time.time_ns()
    print(f'SQRT: N={N} -> {(end - start) / 1000000:>12.4f} ms')

    # C. test only prime divisors
    primes = set()
    def has_no_prime_divisor(n):
        sqrtn = math.sqrt(n)
        for d in primes:
            if d > sqrtn:
                return True
            if n % d == 0:
                False
        return True

    start = time.time_ns()
    result = filter(has_no_prime_divisor, range(2, N + 1))
    for n in result:
        primes.add(n)
        # print(n, end=' ')
    end = time.time_ns()
    print(f'\nPrimes: N={N} -> {(end - start) / 1000000:>12.4f} ms')
