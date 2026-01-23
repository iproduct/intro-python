import math

if __name__ == '__main__':
    fruits = ['apple', 'banana', 'orange', 'cherry', 'papaya']
    for fruit in fruits:
        for ch in fruit:
            print(ch, ' | ', sep='', end='')
        print()

    for i in range(len(fruits)):
        print(fruits[i], end=' ')

    print('\n')

    # primes using for and while
    n = 100
    for i in range(2, n + 1):
        sqrt_i = int(math.sqrt(i))
        d = 2
        while d <= sqrt_i:
            if i % d == 0:
                break
            d += 1
        else:
            print(i, end=', ')

    # primes using for only
    print('\n')
    for i in range(2, n + 1):
        sqrt_i = int(math.sqrt(i))
        for d in range(2, sqrt_i +1):
            if i % d == 0:
                break
        else:
            print(i, end=', ')

    print('\n')
    l = list(range(1, n + 1))
    i = 0
    while i < len(l) and l[i] != 256:
        i += 1
    if i < len(l):
        print(l[i])


