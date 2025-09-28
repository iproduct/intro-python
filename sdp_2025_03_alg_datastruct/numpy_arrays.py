import numpy as np

if __name__ == '__main__':
    a = np.array([[12, 46, 18, 9,], [ 108, 92, 15, 3]], dtype=int)
    print(a)
    print(a.shape)
    at = a.transpose()
    print(at)

    a3 = np.arange(500).reshape(5, 10, -1)
    print(a3)

    a4 = np.arange(12).reshape(3, -1)
    print(a4)
    a5 = np.diag([1, 5, 9, 1])
    print(a5)

    print(a4 @ a5)

    print((a4 @ a5) + np.array([100, 200, 300]).reshape(3,1))

    # ufuncs
    def myadd(x, y):
        return x + y
    myadd = np.frompyfunc(myadd, 2, 1)
    print(myadd(np.arange(12).reshape(3, -1), 100))

