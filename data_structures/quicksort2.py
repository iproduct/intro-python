from random import randint

def quick_sort(a):
    quick_sort_part(a, 0, len(a))

def quick_sort_part(a, from_ind, to_ind):
    if to_ind - from_ind <= 1:  # recursion bottom 1 elem array is sorted
        return
    pivot = a[from_ind]
    store_ind = from_ind + 1
    for i in range(from_ind + 1, to_ind):
        if a[i] < pivot:
            a[store_ind], a[i] = a[i], a[store_ind]
            store_ind += 1
    a[from_ind], a[store_ind-1] = a[store_ind-1], a[from_ind]
    #recursion step
    quick_sort_part(a, from_ind, store_ind - 1)
    quick_sort_part(a, store_ind, to_ind)


if __name__ == '__main__':
    a = [randint(1, 100) for i in range(20)]
    print(a)
    quick_sort(a)
    print('\nAfter sort:')
    print(a)

