def sum2(a, b, *args):
    print(args)
    return sum((a, b) + args)

def transform(*args, transformer = lambda x: x):
    return list(map(transformer, args))

def filter(*args, filter=lambda x: True):
    results = []
    for arg in args:
        if filter(arg):
            results.append(arg)
    return results

def process(*args, flt=lambda x: True, transformer = lambda x: x):
    results = tuple(filter(*args, filter=flt))
    return transform(*results, transformer=transformer)

def reduce(iterable, *, reducer, start_val = None):
    first = True
    accummulator = start_val
    for val in iterable:
        if start_val is None and first:
            accummulator = val
            first = False
            continue
        accummulator = reducer(accummulator, val)
        first = False
    return accummulator


if __name__ == '__main__':
    print(sum2(23, 19))
    print(sum2(23, 19, 75, 42, 8, 105, 92))

    print(transform(23, 19, 75, 42, 8, 105, 92, transformer = lambda x: x * x))
    print(filter(23, 19, 75, 42, 8, 105, 92, filter=lambda x: x % 2 == 0))
    print(filter(23, 19, 75, 42, 8, 105, 92, filter=lambda x: x % 2 != 0))
    print(process(23, 19, 75, 42, 8, 105, 92, flt=lambda x: x % 2 != 0, transformer=lambda x: x*x))
    print(reduce([23, 19, 75, 42, 8, 105, 92], reducer=lambda acc, val: acc + val))
    print(reduce([23, 19, 75, 42, 8, 105, 92], reducer=lambda acc, val: acc + val, start_val=0))
    print(reduce([23, 19, 75, 42, 8, 105, 92], reducer=lambda acc, val: acc * val))
    print(reduce([23, 19, 75, 42, 8, 105, 92], reducer=lambda acc, val: acc * val, start_val=1))
    print(reduce([23, 19, 75, 42, 8, 105, 92], reducer=lambda acc, val: str(acc) + str(val)))
