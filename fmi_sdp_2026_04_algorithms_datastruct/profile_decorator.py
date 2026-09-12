import pstats
from functools import wraps
from io import StringIO
from time import time_ns
from cProfile import Profile


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = Profile()
        flagEnabled = False
        try:
            pr.enable()
            flagEnabled = True
        except:
            pass
        result = func(*args, **kwargs)
        if flagEnabled:
            pr.disable()
            s = StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
            ps.print_stats()
            print(s.getvalue())
        return result

    return wrapper


def profile_naive(unit='ns'):
    def do_profile(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            before = time_ns()
            result = func(*args, **kwargs)
            after = time_ns()
            duration = after - before
            if unit == 'ms':
                duration /= 1000000.0
            print(f'{func.__name__}: {after - before:.6f} {unit}')
            return result

        return wrapper

    return do_profile
