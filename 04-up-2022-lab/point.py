class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

if __name__ == "__main__":
    p1 = Point(4,5)
    print(p1)