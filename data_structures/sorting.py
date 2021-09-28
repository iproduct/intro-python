from array import array
from random import randint

def bubble_sort(a: array):
    n = len(a)
    sorted = False
    i = 0
    while i < n and not sorted:
        sorted = True
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] # swap elements
                sorted = False
        i += 1

def min_selection_sort(a: array):
    pass

def insertion_sort(a: array):
    n = len(a)
    for i in range(n-2, -1, -1):
        index = binary_search(a[i], a, i+1, n)
        ins_index = index - 1 if index >= 0 else -index - 2
        elem = a[i]
        for k in range(i, ins_index):
            a[k] = a[k+1]
        # print(a, index, ins_index, elem)
        a[ins_index] = elem


def binary_search(elem, a: array, frm: int, to: int) -> int:
    while frm < to:
        middle = (frm + to) // 2
        if a[middle] == elem:
            return middle
        elif elem < a[middle]:
            to = middle
        else:
            frm = middle + 1
    else:
        return - to - 1

def quick_sort(a: array):
    quick_sort_rec(a, 0, len(a))

def quick_sort_rec(a: array, frm: int, to: int, level = 0):
    print(f'{" "*2*level}from: {frm} to {to}: {a[frm: to]}')
    if to - frm <= 1: #recursion bottom
        return
    # partitioning elements less than or equal pivot to left, and bigger than pivot to the right
    pivot = a[frm]
    left = frm + 1
    right = to - 1
    while True:
        while left < right and a[left] <= pivot:
            left += 1
        while left <= right and a[right] > pivot:
            right -= 1
        if left < right:
            # print(f'swapping({left}:{a[left]}, {right}:{a[right]})')
            a[left], a[right] = a[right], a[left]
        else:
            break
    a[frm], a[right] = a[right], a[frm]
    # print(pivot, frm, to, left, right, a)

    #recursion step
    quick_sort_rec(a, frm, right, level + 1)
    quick_sort_rec(a, right+1, to, level + 1)

def counting_sort(a:array, min_val: int = 0, max_val: int = 100):
    count = array('I', [0 for i in range(min_val, max_val)])
    for elem in a:
        count[elem - min_val] += 1
    print(count)
    index = 0
    for i in range(len(count)):
        for j in range(count[i]):
            a[index] = i + min_val
            index += 1

if __name__ == '__main__':
    # a = array('I', [64, 125, 17, 35, 72, 5, 13, 8, 63, 17, 54, 63, 95, 7, 14, 63]) #, 9, 75, 46, 3, 1, 46, 167 ,9, 25]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) #[5, 8, 63, 17, 54, 63, 95, 7, 14, 63]) #, 9, 75, 46, 3, 1, 46, 167 ,9, 25])
    a = array('I', [randint(1, 10) for i in range(50)])
    print(a)
    counting_sort(a, 1, 11)
    print(a)
