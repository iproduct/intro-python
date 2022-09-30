a = [12, 53, 4, 5, 6, 7, 829, 10, 14, 37, 14, 53, 17, 9, 42]


def insertion_sort(a):
    i = 1
    n = len(a)
    while i < n:
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        # print(key, i, j, i - j)
        a[j+1] = key
        i += 1


if __name__ == '__main__':
    insertion_sort(a)
    print(a)
