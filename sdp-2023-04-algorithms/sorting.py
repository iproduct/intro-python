from random import randint


def sort_bubble(a):
    swapped = True
    itaration = 0
    while swapped:
        swapped = False
        for i in range(len(a) - itaration - 1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        itaration += 1


def sort_select_min(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        min_val = a[i]
        for j in range(i, n):
            if(a[j] < min_val):
                min_index = j
                min_val = a[j]
        a[i], a[min_index] = a[min_index], a[i]


def sort_ins(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = key


def quick_sort(a, start = 0, end = None):
    if end == None:
        end = len(a)
    if end - start <= 1:   # recursion bottom
        return
    pivot = a[end - 1]
    i = start
    j = end - 2
    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] > pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    a[j + 1], a[end - 1] = a[end - 1], a[j + 1]
    quick_sort(a, start, j + 1)
    quick_sort(a, j + 2, end)


if __name__ == '__main__':
    a = [1222, 315, 433, 12, 7, 52, 610, 42, 34, 72, 320, 95]
    quick_sort(a)
    print(a)

    a = [randint(1, 100000) for i in range(1000)]
    quick_sort(a)
    print(a)