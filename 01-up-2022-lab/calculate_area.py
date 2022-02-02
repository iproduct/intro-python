import math
def calc_area(points_list: list[tuple]) -> float:
    # Using area formula from: https://www.mathopenref.com/coordpolygonarea.html
    if len(points_list) < 3:
        return 0
    prev_point = points_list[-1]
    sum = 0
    for point in points_list:
        part = prev_point[0] * point[1] - prev_point[1] * point[0]
        sum += part
        prev_point = point
    sum /= 2
    area = abs(sum)
    return area

if __name__ == '__main__':
    n = int(input("Input number of points: "))
    polygon = []
    for i in range(n):
        x = float(input(f"Point[{i + 1}].X = "))
        y = float(input(f"Point[{i + 1}].Y = "))
        polygon.append((x, y))
        if i > 0:
            print(f"Side[{i}] = {math.sqrt((x - previous[0])**2 + (y - previous[1])**2)}")
        previous = (x, y)
    print(f"Area of {polygon} is: {calc_area(polygon)}")
    # polygons = [
    #     [(0, 0), (0, 7), (4, 7), (4, 0)],
    #     [(2, 2), (11, 2), (9, 7), (4, 10)]
    #     ]
    # for poly in polygons:
    #     print(calc_area(poly))
