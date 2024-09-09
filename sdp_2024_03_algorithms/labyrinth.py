
class Labyrinth:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.rows = ['_' * width] * height

    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])

    def load(self, filename):
        with open(filename, 'r') as f:
            lines= f.readlines()
            self.width = len(lines[0])
            self.height = len(lines)
            self.rows.clear()
            for line in lines:
                self.rows.append(line[:-1])

    def save(self, filename):
        with open(filename, 'w') as f:
           for line in self.rows:
               f.write(f'{line}\n')


if __name__ == '__main__':
    # lab = Labyrinth(10,10)
    # print(lab)
    # lab.save('labyrinth01.txt')
    lab = Labyrinth()
    lab.load('labyrinth01.txt')
    print(lab)