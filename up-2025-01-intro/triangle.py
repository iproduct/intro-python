import math

def is_triangle(a : float, b: float, c:float) -> bool:
    max_side = max(a, b, c)
    sum_of_other_sides = sum([a, b, c]) - max_side
    return sum_of_other_sides > max_side

def area(a : float, b: float, c:float) -> float:
    math.sqrt()
    return 0.0

if __name__ == "__main__":
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    print(is_triangle(a, b, c))
    print(area(a, b, c))