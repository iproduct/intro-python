from idlelib import hyperparser
from math import hypot
from typing import Self


class Point(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: Self) -> float:
        return hypot(self.x - other.x, self.y - other.y)


def input_points() -> list[Point]:
    i = 0
    l_points = []
    while True:
        print(f'Input point {i} coordinates (<Enter> for exit)')
        coord_str = input(f'Input P[{i}] X,Y: ')
        if not coord_str:
            break
        try:
            (x, y) = map(float, coord_str.split(','))
            l_points.append(Point(x, y))
            i += 1
        except ValueError:
            print(f'Invalid coordinates input "{coord_str}" - ex.: 2.4,3.8')
    return l_points


def get_perimeter(l_points: list[Point]) -> float:
    p = 0
    n = len(l_points)
    for i in range(n):
        p += l_points[i].distance(l_points[(i + 1) % n])
    return p

if __name__ == '__main__':
    l_points = input_points()
    print(get_perimeter(l_points))