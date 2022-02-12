import cProfile
import io
import pstats
from functools import wraps

def profile(fnc):
    @wraps(fnc)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        ret_val = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return ret_val
    return wrapper