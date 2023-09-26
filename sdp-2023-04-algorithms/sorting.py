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
        j = i - 1
        while j >= 0 and a[j] >= a[i]:
            j -= 1
        temp = a[i]
        for k in range(i, j + 1, -1):
            a[k] = a[k - 1]
        a[j + 1] = temp

if __name__ == '__main__':
    a = [1222, 315, 433, 12, 7, 52, 610, 42, 34, 72, 320, 95]
    sort_ins(a)
    print(a)

    a = [randint(1, 100000) for i in range(1000)]
    sort_ins(a)
    print(a)