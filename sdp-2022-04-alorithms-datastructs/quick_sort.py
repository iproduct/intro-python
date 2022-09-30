import random
# a = [12, 53, 4, 5, 6, 7, 829, 10, 14, 37, 14, 53, 17, 9, 42]

a= []
for i in range(50):
    a.append(random.randint(1,100))

def quick_sort_impl(a, start, end):
    if end - start < 2: return
    pivot = a[end-1]
    i =  start
    j = end-2
    while i <= j:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] > pivot:
            j -= 1
        # print(i, '->', a[i], ' | ',  j,  '->', a[j])
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    a[j+1] , a[end -1] = a[end-1], a[j+1]
    # print(pivot, ':', i, j, '->', a[start:end])
    quick_sort_impl(a, start, j+1)
    quick_sort_impl(a, j+2, end)

def quick_sort(a):
    quick_sort_impl(a, 0, len(a))


if __name__ == '__main__':
    quick_sort(a)
    print(a)
