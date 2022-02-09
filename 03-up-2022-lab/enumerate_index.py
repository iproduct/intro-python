from typing import Iterator, TypeVar

T = TypeVar('T')


def index(iter: Iterator[T], start: int = 0, step: int = 1) -> Iterator[tuple[int, T]]:
    i = start
    for elem in iter:
        yield i, elem
        i += step


if __name__ == '__main__':
    for i, ch in index("I love Python!", 1):
        print(i, ":", ch)

    for i, ch in enumerate("I love Python!", 1):
        print(i, ":", ch)
