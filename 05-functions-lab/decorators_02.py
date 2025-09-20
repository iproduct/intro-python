import random
from functools import update_wrapper, wraps
from logging import Logger
from time import time_ns
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
            result = delegate(*args, **kwargs) # call the delegate function
            print(f"--> Delegate '{delegate.__name__}' returned"
                  + (f" result: {result}" if print_result else ""))
            return result

        return wrapper

    return logged_decoratror

def profile(unit="ns"):
    def do_profile(delegate):
        @wraps(delegate)
        def wrapper(*args, **kwargs):
            before = time_ns()
            result = delegate(*args, **kwargs)  # call the delegate function
            after = time_ns()
            exec_time = after - before
            if unit == "ms":
                exec_time /= 1000000
            print(f"Function '{delegate.__name__}' executed for: {exec_time} {unit}")
            return result
        return wrapper
    return do_profile


@logged()
@profile("ms")
def print_name(name: str, congrat="Hi") -> str:
    sum = 0
    for i in range(100000000):
        sum += i
    print(name)
    return name.upper()

# @repeat(times=10) # TODO: implement it
# def print_random_int():
#     print(random.randint(1,100))


if __name__ == '__main__':
    # factory = my_decorator_factory("Zdravei")
    # function = factory(print_name)
    # result = function("Trayan")
    # my_decorator_factory("Zdravei")(print_name)("Trayan")
    # my_decorator(print_name)("Trayan")
    print_name("Trayan", congrat="Hello")
    print("Called function:", print_name.__name__)
