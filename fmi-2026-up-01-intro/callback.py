from typing import Callable


def calculate(i: int, j: int, operand: Callable[[int, int], int]) -> int:
    return operand(i, y = j)


def plus(x: int, /, y: int) -> int:
    return x + y


def reminder(x: int, y: int) -> int:
    return x % y


if __name__ == "__main__":
    print(calculate(21, 5, plus))
    print(calculate(21, 5, reminder))
    print(calculate(21, 5, lambda x, y: x * y))
    divide = lambda x, y: x // y
    print(calculate(21, 5, divide))
