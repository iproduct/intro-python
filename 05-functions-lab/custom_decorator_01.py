from functools import wraps, update_wrapper

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)

    return  wrapper
    # return update_wrapper(wrapper, f)


@my_decorator
def example(*args, **kwargs):
    """Docstring"""
    return f"Called example function: {args}, {kwargs}"

if __name__ == '__main__':
    print(example(1, 2, 3, title="abc"), ", function name:", example.__name__)