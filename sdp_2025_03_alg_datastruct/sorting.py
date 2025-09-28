def sort_bubble[T](arr: list[T]):
    swap = True
    i = 0
    while swap:
        swap = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        i += 1
    print(f'Iterations: {i}')


def sort_select_min[T](arr: list[T]):
    for i in range(len(arr) - 1):
        index_min = i
        min = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                index_min = j
                min = arr[j]
        arr[i], arr[index_min] = arr[index_min], arr[i]


def sort_ins[T](arr: list[T]):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while  j >= 0 and current < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1

def quick_sort[T](arr: list[T], start = 0, end = None):
    if end is None:
        end = len(arr)
    if end - start <= 1: # recursion bottom
        return
    pivot = arr[end - 1]
    i = start
    j = end - 2
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j+1], arr[end-1] = arr[end-1], arr[j+1]
    quick_sort(arr, start, j+ 1)
    quick_sort(arr, j+2, end)


MAX_VALUE = 101
def counting_sort[T](arr: list[T]):
    counts = [0] * MAX_VALUE
    for elem in arr:
        counts[elem] += 1
    arr.clear()
    for i in range(MAX_VALUE):
        for j in range(counts[i]):
            arr.append(i)


if __name__ == '__main__':
    a = [12, 46, 18, 9, 100, 92, 15, 9, 50, 40, 50, 20, 9, 12, 3, 50, 17, 100, 30, 7, 46, 9, 50, 70, 3, 1]
    # a = [9, 12, 46, 108, 92, 15, 150, 170]
    counting_sort(a)
    print(a)
