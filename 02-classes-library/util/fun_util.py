from typing import Iterable, Callable


def find(iterable: Iterable, predicate: Callable[[object], bool]) -> object | None:
    for item in iterable:
        if predicate(item):
            return item
    return None
