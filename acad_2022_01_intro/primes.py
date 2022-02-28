

def find_primes(n):
    """
    Returns all prime numbers between 2 and n
    :param n: the upper bound
    :return: sequence of all prime numbers less or equal to n
    """
    # numbers = [bool(x) for x in range(2, n+1)]
    numbers = [True] * (n-1)
    primes = []
    i = 0
    while i < n - 1:
        while i < n - 1 and numbers[i] is False: # find first number that is True
            i += 1
        if i >= n-1:
            break
        prime = i + 2
        primes.append(prime)
        if prime * prime <= n:
            j = i
            while j < n-1:
                numbers[j] = False
                j += prime
        i += 1
    return primes


if __name__ == '__main__':
    print(find_primes(997))