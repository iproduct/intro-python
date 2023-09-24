from typing import Callable

def logged(print_args = True, print_result = True) -> Callable:
    def logged_instance(delegate: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f'Callinhg {delegate.__name__}', end='')
            if print_args:
                print(f' with arguments: {args} and {kwargs}', end='')
            result = delegate(*args, **kwargs)
            if print_result:
                print(' -> ', result)
            else:
                print()
            return result

        return wrapper

    return logged_instance