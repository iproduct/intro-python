from typing import Protocol


class Shape(Protocol):
    """Any class with an area() method satisfies this protocol."""

    def area(self) -> float:
        ...


class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)


def print_area(figure: Shape) -> None:
    print(f"The area is: {figure.area()}")


# Both Square and Circle work, even though they don't inherit from Shape
print_area(Square(5))  # Output: 25.0
print_area(Circle(3))  # Output: 28.27...