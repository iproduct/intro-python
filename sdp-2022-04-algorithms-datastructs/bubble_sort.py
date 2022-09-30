a = [12, 53, 4, 5, 6, 7, 829, 10, 14, 37, 14, 53, 17, 9, 42]


def bubble_sort(a):
    sorted = False
    i = 0
    n = len(a)
    while not sorted or i < n - 1:
        j = 0
        sorted = True
        while j < n - i - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                sorted = False
            j += 1
        i += 1


if __name__ == '__main__':
    bubble_sort(a)
    print(a)
