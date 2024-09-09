
class Labyrinth:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.rows = [[0] * width] * height

    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])

if __name__ == '__main__':
    lab = Labyrinth(10,10)
    print(lab)