from random import randint

def insertion_sort(a):
    for key_ind in range(1, len(a)):
        key = a[key_ind]
        i = key_ind - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        else:
            a[i + 1] = key


if __name__ == '__main__':
    a = [randint(1, 100) for i in range(20)]
    print(a)
    insertion_sort(a)
    print('\nAfter sort:')
    print(a)

