import numpy as np

if __name__ == '__main__':
    a = np.array([[5, 8, 17, 54, 63, 95, 7, 14, 9], [23, 56, 67, 9, 19, 3, 23 ,45, 78], [34, 67, 8, 2, 45, 45, 67, 82, 1]])
    a[0][3] = 75
    a[1,0] += 1
    print(a)
    print(a.ndim, a.shape, a.dtype)
    print(a[:2, -4:])
    b = a.reshape((1, 27))
    print(b)
    c = a[0]
    print(c)