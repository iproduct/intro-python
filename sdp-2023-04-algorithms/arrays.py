from array import array

if __name__ == '__main__':
    a = array('i', [1222, 315, 433, 12, 7, 52, 610])
    with open('array.bin', 'wb') as f:
        a.tofile(f)
    with open('array.bin', 'rb') as f:
        b = array('i')
        b.fromfile(f, len(a))
    print(b)
