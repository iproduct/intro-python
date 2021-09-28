from array import array

if __name__ == '__main__':
    a = array('I', [5, 8, 17, 54, 63, 95, 7, 14, 9])
    a[3] = 75
    a[0] += 1
    print(a)