import array as arr

a = arr.array('i', [2, 4, 6, 8])

if __name__ == '__main__':
    a[0] = 10
    a[1] = 12
    a[3] = a[2] + 5
    print(len(a)) # Length of the array
    print(a)
