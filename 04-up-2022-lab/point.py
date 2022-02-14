from __future__ import annotations

import math


class Point(object):
    """
    Point models a 2D point in Decart plain
    """
    next_id = 0

    @classmethod
    def get_next_id(cls):
        """ returns number of points created so far"""
        cls.next_id += 1
        return cls.next_id

    def __init__(self, x=0, y=0):
        """
        Initialize point coordinates and id
        :param x: x coordinate
        :param y: y coordinate
        """
        self.id = self.get_next_id()
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.id}: {self.x},{self.y})"
    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def distance_to(self, other: Point) -> float:
        """
        returns the distance between self and other points
        :param other: the point to calculate distance to
        :return: the distance between two points
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

if __name__ == "__main__":
    p1 = Point(4, 5)
    p2 = Point(0, 9)
    p3 = Point(1, 1)
    print(p1)
    print(p2)
    print(p3)
    print(p1.distance_to(p3))
    print(p3.distance_to(p1))
    print("Number of Pints created:", p1.next_id)
    print("Number of Pints created:", p1.__class__.next_id)
    print("Number of Pints created:", Point.next_id)
    print(p1 + p3)
