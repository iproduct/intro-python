from typing import Iterator, TypeVar


def numbers(start: int, end: int, step: int = 1) -> Iterator[int]:
    i = start
    while i < end:
        yield i
        i += step


class numbers_iterator(Iterator):
    def __init__(self, start: int, end: int, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        result = self.value
        if result < self.end:
            self.value += self.step
            return result
        else:
            raise StopIteration()


if __name__ == '__main__':
    iterator = iter(numbers_iterator(0, 20, 3))
    while True:
        try:
            n = next(iterator)
        except StopIteration:
            break
        print(n)

    iterator = iter(numbers(0, 20, 3))
    while True:
        try:
            n = next(iterator)
        except StopIteration:
            break
        print(n)

    for i in numbers(0, 20, 3):
        print(i)

    for i in numbers_iterator(0, 20, 3):
        print(i)
