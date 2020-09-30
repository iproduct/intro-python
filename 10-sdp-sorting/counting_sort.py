from random import randint

def counting_sort(a, min_value, max_value):
    bin = [0] * (max_value - min_value)

    for i in range(len(a)): # N = len(a) iterations
        bin[(a[i] - min_value)] += 1 # M = (max_value - min_value) elements in memory

    i = 0
    for j in range(max_value - min_value): # N
        for k in range(bin[j]):
            a[i] = j + min_value
            i += 1


if __name__ == '__main__':
    a = [randint(1, 10) for i in range(20)]
    print(a)
    counting_sort(a, 1, 11)
    print('\nAfter sort:')
    print(a)

