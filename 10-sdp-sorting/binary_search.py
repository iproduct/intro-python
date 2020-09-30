from random import randint

def binary_search(a, value):
    left = 0
    right = len(a) - 1
    while right - left > 0:
        mid = (left + right) // 2
        if(a[mid] < value):
            left = mid + 1
        else:
            right = mid
    if a[left] == value:
        return left
    else:
        return -left - 1;

if __name__ == '__main__':
    a = [randint(1, 100) for i in range(20)]
    print(a)
    a.sort()
    print('\nAfter sort:')
    print(a)
    value = int(input('Search for value:'))
    print(f'Index: {binary_search(a, value)}')

