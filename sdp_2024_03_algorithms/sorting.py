from random import randint


def sort_bubble(a: list[int]):
    is_sorted = False
    i = 0
    while not is_sorted and i < len(a) - 1:
        is_sorted = True
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                is_sorted = False
        i += 1


def sort_selection_min(a: list[int]):
    for i in range(len(a) - 1):
        min_val = a[i]
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < min_val:
                min_val = a[j]
                min_index = j
        a[min_index], a[i] = a[i], a[min_index]

def sort_insertion(a: list[int]):
    for i in range(len(a) - 1):
        key = a[i]
        j = i - 1
        while key < a[j] and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j + 1] = key


def quicksort(a: list[int]):
    quicksort_rec(a, 0, len(a))

def quicksort_rec(a: list[int], left, right):
    # print(f'{left}, {right} :{a}')
    if left >= right - 1: #recursion bottom
        return

    pivot = a[left] # recursion step
    i = left
    j = right
    while i <= j:
        while True:
            i += 1
            if i >= j or a[i] >= pivot :
                break
        while True:
            j -= 1
            if i >= j or a[j] <= pivot :
                break
        # print(f'i={i}, j={j}')
        if i < j:
            a[i], a[j] = a[j], a[i]
    # print(f'Swap: i={i}, j={j}')
    a[j], a[left] = a[left], a[j]
    # print(f'After: {a[left: right]}, {left}, {right}, Pivot = {pivot} -> {j}')
    quicksort_rec(a, left, j)
    quicksort_rec(a, j+1, right)





if __name__ == '__main__':
    a = []
    for i in range(100):
        a.append(randint(1, 100))
    # a = [73, 4, 45, 39, 86, 82, 7, 54, 94, 91, 16, 59, 74, 73, 39, 35, 69, 62, 31, 98, 14, 57, 75, 27, 26, 11, 24, 20, 18, 77, 27, 58, 74, 64, 77, 10, 1, 11, 100, 100, 15, 11, 62, 67, 40, 11, 54, 73, 32, 73, 69, 19, 67, 86, 24, 34, 69, 84, 72, 37, 80, 61, 9, 68, 83, 27, 45, 60, 29, 94, 38, 69, 78, 9, 69, 94, 78, 73, 63, 5, 83, 3, 68, 81, 26, 17, 89, 50, 96, 100, 13, 32, 68, 44, 27, 74, 14, 79, 15, 73]
    print(a)
    quicksort(a)
    print(a)