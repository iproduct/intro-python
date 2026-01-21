def print_primes(n):
    sieve = [True] * (n+1)
    for i in range(2, n):
        if sieve[i]:
            print(i, end=', ')
        for j in range(i * i, n + 1, i):
            sieve[j] = False

if __name__ == '__main__':
    n = int(input('Input a number: '))
    print_primes(n)

