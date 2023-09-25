import time

def profile(f):
    def wrapper(*args, **kwargs):
        before = time.time_ns()
        result = f(*args, **kwargs)
        after = time.time_ns()
        exec_time = after - before
        print(f'Function \'{f.__name__}\' executed for: {exec_time} ns')
        return result
    return wrapper