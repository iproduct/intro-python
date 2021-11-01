import cProfile
import io
import pstats

import numpy as np


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


def f(x):
    return x or "default"


def remove_by_index(l, index):
    """removes element at index position from indexed sequence l and returns the result as new object"""
    return l[:index] + l[index + 1:]

def remove_by_index_np(l, index):
    """removes element at index position from indexed sequence l and returns the result as new object"""
    return np.concatenate([l[:index], l[index + 1:]])


def pop_by_index(l, index):
    """pops and removes element at index position from indexed sequence l and returns removed element"""
    return l.pop(index)


def del_by_index(l, index):
    """deletes an element at index position from indexed sequence l"""
    del l[index]

def remove_by_index_dict(d, index):
    """deletes an element at index position from indexed sequence l"""
    d[index] = None


@profile
def test_remove_by_index(mylist, iterations):
    def f(l):
        n = 0
        ml = l
        for i in range(0, len(l), 3):
            ml = remove_by_index(ml, i - n)
            n += 1
        return ml

    k = 0
    while k < iterations:
        k += 1
        f(mylist.copy())


@profile
def test_remove_by_index_np(mylist, iterations):
    def f(l):
        n = 0
        ml = l
        for i in range(0, len(l), 3):
            ml = remove_by_index_np(ml, i - n)
            n += 1
        return ml

    k = 0
    while k < iterations:
        k += 1
        f(np.array(mylist))


@profile
def test_pop_by_index(mylist, iterations):
    def f(l):
        n = 0
        for i in range(0, len(l), 3):
            pop_by_index(l, i - n)
            n += 1
        return l

    k = 0
    while k < iterations:
        k += 1
        f(mylist.copy())


@profile
def test_del_by_index(mylist, iterations):
    def f(l):
        n = 0
        for i in range(0, len(l), 3):
            del_by_index(l, i - n)
            n += 1
        return l

    k = 0
    while k < iterations:
        k += 1
        f(mylist.copy())

@profile
def test_remove_by_index_dict(mydict: dict, iterations):
    def f(d):
        n = 0
        for i in range(0, len(d), 3):
            remove_by_index_dict(d, i - n)
            n += 1
        return d

    k = 0
    while k < iterations:
        k += 1
        f(mydict.copy())


if __name__ == '__main__':
    n = 10000
    iters = 100
    mylist = [x for x in range(n)]
    test_remove_by_index(mylist, iters)
    mylist = [x for x in range(n)]
    test_remove_by_index_np(mylist, iters)
    mylist = [x for x in range(n)]
    test_pop_by_index(mylist, iters)
    mylist = [x for x in range(n)]
    test_del_by_index(mylist, iters)
    mydict = {x: x for x in range(n)}
    test_remove_by_index_dict(mylist, iters)
