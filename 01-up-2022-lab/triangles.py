import math


def distance(ax, ay, bx, by):
    return math.sqrt((ax - bx) * (ax - bx) + (ay - by) * (ay - by))


def input_float(message):
    while True:
        data = float(input(message))
        if 0 <= data <= 100:
            return data
        print("Error: Coordinates should be between 0 and 100.")


if __name__ == '__main__':
    n = int(input("Input number of triangles: "))
    triangles = []
    # reading triangle coordinates
    for i in range(n):
        print(f"Enter triangle {i + 1} coordinates:")
        x1 = input_float(f"Point[1].X = ")
        y1 = input_float(f"Point[1].Y = ")
        x2 = input_float(f"Point[2].X = ")
        y2 = input_float(f"Point[2].Y = ")
        x3 = input_float(f"Point[3].X = ")
        y3 = input_float(f"Point[3].Y = ")
        triangles.append((x1, y1, x2, y2, x3, y3))

    # calculate sides and check if triangle
    for t in triangles:
        # (x1, y1, x2, y2, x3, y3) = t
        a = distance(t[0], t[1], t[2], t[3])
        b = distance(t[2], t[3], t[4], t[5])
        c = distance(t[4], t[5], t[0], t[1])
        print(f"Sides of trianle {t} are: {a}, {b}, {c}")
        if a + b <= c or b + c <= a or c + a <= b:
            print(f"Coordinates {t} do not form a valid triangle.")
        else:
            # calculate the triangle area
            p = (a + b + c) / 2
            area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 8)
            print(f"Area of triangle {t} is: {area}")
