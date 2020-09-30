from random import randint

def bubblesort(a):
    swapped = True
    n = len(a)
    to = n - 1
    while swapped and to > 1:
        swapped = False
        for i in range(to):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]  # swap a[i] and a[i+1]
                swapped = True

if __name__ == '__main__':
    a = [randint(1, 100) for i in range(20)]
    print(a)
    bubblesort(a)
    print('\nAfter sort:')
    print(a)

