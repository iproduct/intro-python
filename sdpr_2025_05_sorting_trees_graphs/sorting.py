def bubble_sort[T](array: list[T]):
    for i in range(len(array) - 1):
        is_sorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                is_sorted = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if is_sorted:
            break

def selection_min_sort[T](array: list[T]):
    for i in range(len(array) - 1):
        min_index = i
        min_val = array[i]
        for j in range(i + 1, len(array)):
            if array[j] < min_val:
                min_index = j
                min_val = array[j]
        array[i], array[min_index] = array[min_index], array[i]

def insertion_sort[T](array: list[T]):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and current < array[j]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1

def quick_sort[T](array: list[T], start: int = 0, end: int = None):
    if end is None:
        end = len(array)
    if end - start <= 1:
        return
    pivot = array[end - 1]
    i = start
    j = end - 2
    while i <= j:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
        array[j+1], array[end-1] = array[end-1], array[j+1]
    quick_sort(array, start, j + 1)
    quick_sort(array, j + 2, end)

MAX_VALUE = 301

def counting_sort[T](array: list[T]): # O(N + MAX_VALUE)
    counts = [0] * MAX_VALUE
    for elem in array:
        counts[elem] += 1
    k = 0
    for i in range(MAX_VALUE):
        for j in range(counts[i]):
            array[k] = i
            k += 1

def merge_sort[T](array: list[T]):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

if __name__ == '__main__':
    a = [213, 12, 5, 17, 8, 29, 54, 82, 1, 7, 1, 2, 67, 2, 17, 3, 14, 7, 18, 171, 17]
    merge_sort(a)
    print(a)
