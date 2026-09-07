from functools import wraps


def simple_decorator(f):
    @wraps(f)  # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs) :
        print(f'-- before delegate: {args}, {kwargs} --')
        result = f(*args, **kwargs)
        print(f'-- after delegate: {args}, {kwargs} -> {result} --')
        return result
    return wrapper


@simple_decorator
def fib_rec(n):
    """Fibonacci numbers up to n"""
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

if __name__ == '__main__':
    print('Fib[6] = ', fib_rec(6))
    print('fib_rec name:', fib_rec.__name__, 'Docstring: ', fib_rec.__doc__)
