from functools import wraps


def trace(func):
    print('Trace decorator instantiated')
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling function "{func.__name__}" with:', *args, **kwargs)
        result = func(*args, **kwargs)
        print(f'Returning from "{func.__name__}" with result:', result)
        return result
    return wrapper