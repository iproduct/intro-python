import cProfile, pstats, io, time
import re
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
    # print(f("hello"))
    # print(" | ".join(["Python", "is", "easy"]))
    # print(f'Result is {f("hello")}')
    # print('Result is: %s' % f("hello"))
    # result = f("hello")
    # print('Result is: %s, len=%d' % (result, len(result)))
    # print('Result is: len = %(length)d, name=%(name)s' % {"name": result, "length": len(result)})
    date_str = "12.07.1982"
    print(re.split("",date_str))
    sum = 0
    for ch in re.split("",date_str):
        sum += int(ch) if ch.isdigit() else 0
    print(sum)
    # date_result = date_str[:2] + date_str[3:5] + date_str[6:]
    # print(date_result)
    #
    # sum = 0
    # for ch in date_str:
    #     if ch != '.':
    #         sum += int(ch)
    # print(f'Sum1 = {sum}')
    #
    # digits_list = list(date_str)
    # print(digits_list)
    # sum = 0
    # for ch in digits_list:
    #     if ch != '.':
    #         sum += int(ch)
    # print(f'Sum2 = {sum}')
    #
    # sum = 0
    # for ch in date_str:
    #     sum += int(ch) if ch != '.' else 0
    # print(f'Sum3 = {sum}')
    #
    # sum = 0
    # parts = date_str.split(sep=".")
    # print(parts)
    # for part in parts:
    #     for digit in part:
    #         # print(digit)
    #         sum += int(digit)
    # print(f'Sum4 = {sum}')
    #
    # # remove element by remove_by_index
    # digits_list = list(date_str)
    # print(remove_by_index(digits_list, 3))  # does not mutate original list
    # print(digits_list)
    #
    # print(digits_list.pop(3))  # mutate original list
    # print(digits_list)
    #
    # for d in set(date_str):
    #     print(d)

    n = 10000
    iters = 1000
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
