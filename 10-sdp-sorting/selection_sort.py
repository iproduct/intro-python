from random import randint

def selection_sort_min(a):
    n = len(a)
    for from_ind in range(0, n - 1):
        min_ind = from_ind
        # find index of the minimal element
        for i in range(from_ind, n):
           if a[i] < a[min_ind]:
               min_ind = i
        a[from_ind], a[min_ind] = a[min_ind], a[from_ind]  # swap a[from_ind] and min element

# Homework: selection_sort_max(a)

if __name__ == '__main__':
    a = [randint(1, 100) for i in range(20)]
    print(a)
    selection_sort_min(a)
    print('\nAfter sort:')
    print(a)

