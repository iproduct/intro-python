a = [12, 53, 4, 5, 6, 7, 829, 10, 14, 37, 14, 53, 17, 9, 42]


def selection_max_sort(a):
    i = 0
    n = len(a)
    while i < n - 1:
        j = 1
        max = a[0]
        max_index = 0
        while j < n-i:
            if a[j] > max:
                max = a[j]
                max_index = j
            j += 1
        print(max_index, n - i)
        a[max_index], a[n-i-1] = a[n-i-1], a[max_index]
        i += 1

if __name__ == '__main__':
    selection_max_sort(a)
    print(a)
