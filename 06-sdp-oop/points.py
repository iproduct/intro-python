import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<{self.x},{self.y}>'

    def __copy__(self):
        return type(self)(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return type(self)(self.x - other.x, self.y - other.y)

    def distance(self, other):
        if isinstance(other, Point):
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        else:
            raise TypeError('Invalid argument type')


if __name__ == '__main__':
    p1 = Point(2,2)
    p2 = Point(5,6)
    p3 = p1 + p2

    print(p1, p2, p3, p2 - p1)
    print(f'Distenace betwen {p1} and {p2} is: {p1.distance(p2)}')