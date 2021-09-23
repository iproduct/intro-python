import time

def sampledec(f):
    print('invoking decorator')
    return f

def profile(nanos = False):
    def outer_wrapper(f):
        def wrapper(*args, **kwargs):
            print(f'-- start profiling {f.__name__}')
            start_time = time.time_ns()
            f(*args, **kwargs)
            end_time = time.time_ns()
            if nanos:
                print(f'-- end profiling {f.__name__}, execution time: {end_time - start_time} ns')
            else:
                print(f'-- end profiling {f.__name__}, execution time: {(end_time - start_time) // 1000} ms')
        return wrapper
    return outer_wrapper

@profile(nanos = False)
def myfunc(n):
    sum = 0
    for i in range (1000000):
        sum += i
    print(f'invocing myfunc({n}): {sum}')

if __name__ == '__main__':
    myfunc(12)