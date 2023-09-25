import cProfile
import io
import pstats
import time

def timer(f):
    def wrapper(*args, **kwargs):
        before = time.time_ns()
        result = f(*args, **kwargs)
        after = time.time_ns()
        exec_time = (after - before) / 1000000
        print(f'Function \'{f.__name__}\' executed for: {exec_time} ms')
        return result
    return wrapper


def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner