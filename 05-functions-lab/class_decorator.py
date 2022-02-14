from functools import update_wrapper, wraps


class CountCalls:
    def __init__(self, func):
        self.delegate = func
        self.calls_count = 0

    def __call__(self, *args, **kwargs):
        self.calls_count += 1
        print(f"Call {self.calls_count} of {self.delegate.__name__}")
        return self.delegate(*args, **kwargs)

@CountCalls # TODO - Implement me
def say_hello(name):
    print(f"Hello {name}!")

@CountCalls # TODO - Implement me
def say_goodbye(name):
    print(f"Goodbye {name}!")

class process_file:
    """
        Decorator iterates all lines in a text file and processes each line using decorated function
    """
    def __init__(self, filename, mode="r", callback=None):
        """
        Init decorator
        :param filename: file name to process
        :param mode: file open mode
        :param callback: callback is called after processing whole file
        """
        pass #TODO - Implement me

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass #TODO - Implement me
        return wrapper

if __name__ == "__main__":
    say_hello(name="Georgi")
    say_hello("Petar")
    say_goodbye("Maria")
    say_goodbye("Maria")

    @process_file("class_decorator.py", mode="rt")
    def print_comments(line: str):
        index = line.find("#")
        if index >= 0:
            print(line[index:])

    print_comments()
    print(print_comments.__name__)