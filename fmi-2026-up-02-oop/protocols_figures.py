from abc import ABC, abstractmethod
from typing import Protocol, Iterable
import math


class Shape(Protocol):
    """Any class with an area() method satisfies this protocol."""

    def area(self) -> float:
        ...


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

class Ellipse(Shape):
    def __init__(self, diameter1: float, diameter2: float):
        self.diameter1 = diameter1
        self.diameter2 = diameter2

    def area(self) -> float:
        return math.pi * self.diameter1 * self.diameter2 / 4


class Circle(Ellipse):
    def __init__(self, diameter: float):
        # Ellipse.__init__(self,diameter, diameter)
        super().__init__(diameter, diameter)


class Triangle(Shape):
    def __init__(self, side: float):
        self.side = side
    def area(self) -> float:
        return math.sqrt(3)/4 * (self.side**2)


def print_area(figure: Shape) -> None:
    print(f"The {figure.__class__.__name__} area is: {figure.area()}")

def calc_all_areas(figures: Iterable[Shape]) -> Iterable[float]:
    for figure in figures:
        yield figure.area()

if __name__ == "__main__":
    # Both Square and Circle work, even though they don't inherit from Shape
    print_area(Square(5))  # Output: 25.0
    print_area(Ellipse(4,6))  # Output: 28.27...
    print_area(Circle(6))  # Output: 28.27...
    print_area(Triangle(5))  # Output: 28.27...
    figures = [Square(5), Circle(3), Triangle(5)]
    print(list(calc_all_areas(figures)))
    print(list(map(lambda figure: figure.area(), figures)))
    print(sum(map(lambda figure: figure.area(), figures)))

