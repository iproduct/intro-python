import time
from random import randint

from profile_decorator import profile

N = 1000000
ITERATIONS = 1000
def find_index(lst, elem):
    """find index with O(n) time complexity"""
    for i in range(len(lst)):
        if elem == lst[i]:
            return i
    return None

def find_index_sorted(lst, elem, start=0, end=None):
    """find index in sorted list with O(log(n)) time complexity"""
    if end == None:
        end = len(lst)
    length = end - start
    if length == 0:       # recursion bottom
        return None
    moddle_ind = start + length // 2   #recursion step
    middle = lst[moddle_ind]
    if elem == middle :
        return moddle_ind
    elif elem < middle:
        return find_index_sorted(lst, elem, start, moddle_ind)
    else:
        return find_index_sorted(lst, elem, moddle_ind + 1, end)


def perf_test(func, *args):
    exec_times = []
    for i in range(ITERATIONS):
        elem = l[randint(0, N)]
        start = time.time_ns()
        func(*(args+(elem,)))    # call tested function
        end = time.time_ns()
        exec_times.append((end - start) / 1000000)
    return exec_times

def average(lst):
    sum = 0
    for t in lst:
        sum += t
    return sum / len(lst)


if __name__ == '__main__':
    l = [randint(1,100000000) for i in range(N)]
    l.sort()
    times = perf_test(find_index, l)
    print(f'find_index -> {average(times)} : {times}')

    times = perf_test(find_index_sorted, l)
    print(f'find_index_sorted -> {average(times)} : {times}')