def gcd(a, b):
    while b != 0:
        # print('a, b:', a, b)
        a, b = b, a % b
    return a

if __name__ == '__main__':
    print('gcd:', gcd(120, 54))
    print('gcd:', gcd(285, 140))
    print('gcd:', gcd(71, 257))
    print('gcd:', gcd(0, 257))
    print('gcd:', gcd(257, 0))