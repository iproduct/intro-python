import cProfile, pstats, io, time

def factorialIter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorialRec(n):
    if n == 1:
        return 1
    else:
        return n * factorialRec(n - 1)


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

@profile
def factorialRunnerIter(n, times):
    for i in range(times):
        factorialIter(n)

@profile
def factorialRunnerRec(n, times):
    for i in range(times):
        factorialRec(n)

if __name__ == '__main__':
    print(factorialRunnerIter(995, 10000))
    print(factorialRunnerRec(995, 10000))