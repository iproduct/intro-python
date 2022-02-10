from functools import update_wrapper, wraps
from logging import Logger
from typing import Callable


def my_decorator(delegate: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("Before delegate")
        # print(message, end=" ")
        result = delegate(*args, **kwargs)
        print("After delegate")
        return result

    return update_wrapper(wrapper, delegate)
    # return my_decorator


def logged(*, print_args=True, print_result=True):
    def logged_decoratror(delegate: Callable) -> Callable:
        @wraps(delegate)
        def wrapper(*args, **kwargs):
            print(f"Calling delegate: '{delegate.__name__}' " +
                  (f"with arguments: {args}, kwargs: {kwargs}" if print_args else ""))
            result = delegate(*args, **kwargs)
            print(f"--> Delegate '{delegate.__name__}' returned"
                  + (f" result: {result}" if print_result else ""))
            return result

        return wrapper

    return logged_decoratror


@logged()
def print_name(name: str, congrat="Hi") -> str:
    print(name)
    return name.upper()


if __name__ == '__main__':
    # factory = my_decorator_factory("Zdravei")
    # function = factory(print_name)
    # result = function("Trayan")
    # my_decorator_factory("Zdravei")(print_name)("Trayan")
    # my_decorator(print_name)("Trayan")
    print_name("Trayan", congrat="Hello")
    print("Called function:", print_name.__name__)
