import math

def is_prime(n):
    for d in range(2, int(math.sqrt(n))):
        if n % d == 0:  # i is not prime
            return False
    return True

def prime_gen(np):
    n = 2
    while np > 0:
        if is_prime(n):
            yield n
            np -= 1
        n += 1

if __name__ == '__main__':
    for n in prime_gen(10):
        print(n)