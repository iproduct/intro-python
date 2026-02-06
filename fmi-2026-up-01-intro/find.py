import random
from typing import Iterable, Callable


def find[X](seq: Iterable[X], predicate: Callable[[X], bool]) -> X:
    for x in seq:
        if predicate(x):
            return x
    else:
        return None


def find_index[X](seq: Iterable[X], predicate: Callable[[X], bool]) -> int:
    index = 0
    for x in seq:
        if predicate(x):
            return  index
        index += 1
    else:
        return -1


if __name__ == '__main__':
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(numbers)
    print(find_index(numbers, lambda n: n % 3 == 0))