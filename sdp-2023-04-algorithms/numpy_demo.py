import numpy as np

if __name__ == '__main__':
    a = np.array([1222, 315, 433, 12, 7, 52, 610, 42, 34, 72, 320, 95])
    print(a)
    print(a.dtype)
    print(a.shape)
    b = a.reshape((-1, 4))
    print(b)
    print(b.shape)
    c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((3, -1))
    print(c)

    t = np.transpose(b)
    d = np.concatenate((t, c), axis=0)
    print(d.shape)
    print(d)

    a.sort()
    print(a)