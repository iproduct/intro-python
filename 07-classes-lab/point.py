class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<" + self.x.__str__() + "," + self.y.__str__() + ">"

if __name__ == '__main__':
    p = Point(4, 3)
    print(p)
    q = Point(0, 0)
    print(q)
    print(p.distance(q))