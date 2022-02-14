from numba import jit
import numpy as np

from profile_decorator import profile

@jit(nopython=True, cache=True)
def sum2d_jit(arr):
    M, N  = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result

def sum2d(arr):
    M, N  = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i, j]
    return result


@profile
def test(func, *args, count=1000, **kwargs):
    while count:
        func(*args, **kwargs)
        count -= 1


if __name__ == "__main__":
    a = np.random.random((1000, 1000))
    # print(a.shape)
    # print(sum2d(a))
    print(sum2d_jit(a))
    test(sum2d, a, count=10)
    test(sum2d_jit, a, count=10)
