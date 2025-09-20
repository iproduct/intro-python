import numbers
from math import isnan


def absolute_value(func):
    print('Decorator instantiated')
    def wrapper(*args, **kwargs):
        print(f'Calling function "{func.__name__}" with:', *args, **kwargs)
        result = func(*args, **kwargs)
        result = abs(result) if isinstance(result, numbers.Number) else result
        print(f'Returning from "{func.__name__}" with result:', result)
        return result
    return wrapper

@absolute_value
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return -a

if __name__ == '__main__':
    print(fibonacci(11))