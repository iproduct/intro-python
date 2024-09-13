from random import randint


def list_gen(n):
    l = []
    for i in range(n):
        l.append(randint(1,100))
    return l

def binary_search(val, l, start, end):
    # print(start, end, l[start: end] )
    if start >= end:
        return -start -1
    mid = (start + end) // 2
    if l[mid] == val:
        return mid
    if val < l[mid]:
        return binary_search(val, l, start, mid)
    else:
        return binary_search(val, l, mid+1, end)

def binary_search_iter(val, l, start, end):
    while start < end:
        # print(start, end, l[start: end])
        mid = (start + end) // 2
        if l[mid] == val:
            return mid
        if val < l[mid]:
            end = mid
        else:
            start = mid + 1
    return -start -1

if __name__ == '__main__':
    # l = list_gen(100)
    l = [90, 89, 36, 87, 63, 36, 71, 99, 37, 72, 17, 73, 26, 16, 51, 14, 10, 39, 46, 45, 60, 78, 58, 58, 2, 62, 63, 88, 92, 91, 83, 47, 19, 62, 52, 20, 19, 86, 2, 36, 19, 73, 49, 67, 85, 56, 8, 73, 47, 98, 2, 33, 72, 34, 95, 37, 49, 55, 18, 13, 17, 82, 33, 83, 33, 79, 22, 12, 28, 66, 54, 55, 66, 47, 62, 78, 94, 26, 27, 1, 19, 95, 47, 28, 54, 83, 91, 63, 30, 25, 28, 3, 73, 72, 71, 20, 69, 59, 52, 61]
    l.sort()
    print(l)
    print(binary_search_iter(11, l, 0, len(l)))