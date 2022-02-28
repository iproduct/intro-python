

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
        # find first number that is True - it is the next prime
        while i < n - 1 and numbers[i] is False:
            i += 1
        if i >= n-1:
            break

        # we have found the index i of the next prime num ber (i == prime - 2)
        prime = i + 2
        primes.append(prime)

        # Set all numbers that are divided by prime to False, but only for primes <= sqrt(n)
        if prime * prime <= n:
            j = i
            while j < n-1:
                numbers[j] = False
                j += prime
        i += 1
    return primes


if __name__ == '__main__':
    print(find_primes(997))