from __future__ import annotations
from point import Point


class PolygonIterator:
    def __init__(self, polygon: Polygon):
        self.polygon = polygon
        self.position = -1

    def __next__(self):
        self.position += 1
        if self.position >= len(self.polygon):
            raise StopIteration()
        return self.polygon[self.position]



class Polygon:
    def __init__(self, *points: Point):
        self.vertices = points # composition - has_a, multiplicity 3..*

    def __len__(self):
        return len(self.vertices)

    def __getitem__(self, index):
        return self.vertices[index]

    # def __iter__(self):
    #     return PolygonIterator(self)

    def __iter__(self):
        for v in self.vertices:
            yield v

    def area(self) -> float:
        # TODO implement this using formula:
        # Area (A) = | (x1y2 – y1x2) + (x2y3 – y2x3)…. + (xny1 – ynx1) | / 2
        return 0

if __name__ == "__main__":
    p1 = Point(4, 5)
    p2 = Point(4, 0)
    p3 = Point(0, 0)
    triangle = Polygon(p1, p2, p3)
    print(f"Triangle has {len(triangle)} points:")
    for p in triangle:
        print(p)
    print("Area =", triangle) # expect: 10