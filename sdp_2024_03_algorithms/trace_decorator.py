from time import time_ns


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} is called with {args}, {kwargs}.')
        result = func(*args, **kwargs)
        print(f'{func.__name__} has returned the result: {result}')
        return result
    return wrapper

def profile(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} is called with {args}, {kwargs}.')
        start = time_ns()
        result = func(*args, **kwargs)
        end = time_ns()
        print(f'{func.__name__} has returned after {(end - start)/1000000} ms')
        return result
    return wrapper

@profile
def fn1(x, y):
    z= 0
    for i in range(1000000):
        z+=1
    return x + y

@profile
def fn2(x, y):
    z = 0
    for i in range(100000):
        z += 1
    return x * y

if __name__ == '__main__':
    fn2(fn1(fn2(3,5), 2), 4)