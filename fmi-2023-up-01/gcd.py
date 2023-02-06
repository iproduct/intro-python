def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    a = int(input('a = '))
    b = int(input('b = '))
    print(f'GCD({a},{b}) = {gcd(a, b)}')