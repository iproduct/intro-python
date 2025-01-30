def gcd(a, b):
    if a == 0:
        return b
    return gcd(b, a % b)


def gcd_iter(a, b):
    while b > 0:
        print(f'(a, b) = ({a}, {b})')
        a, b = b, a % b
    return a


if __name__ == '__main__':
    a, b = 28, 75
    print(f'GCD({a}, {b}) = {gcd_iter(a, b)}')
