import math
import random


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return  a

if __name__ == '__main__':
    for i in range(1000):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f'a={a}, b={b} -> math.gcd={math.gcd(a,b)}, myGCD = {gcd(a,b)}')