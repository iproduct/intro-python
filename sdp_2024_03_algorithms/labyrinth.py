
class Labyrinth:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__rows = ['_' * width] * height

    def __str__(self):
        return '\n'.join([str(row) for row in self.__rows])

    def get_cell(self, col, row):
        return self.__rows[row][col]

    def is_free(self, col, row) -> bool:
        return self.__rows[row][col] == '_'

    def load(self, filename):
        with open(filename, 'r') as f:
            lines= f.readlines()
            self.width = len(lines[0]) - 1
            self.height = len(lines)
            self.__rows.clear()
            for line in lines:
                self.__rows.append(line[:-1])

    def save(self, filename):
        with open(filename, 'w') as f:
           for line in self.__rows:
               f.write(f'{line}\n')


class FindPath:
    def __init__(self, labyrinth: Labyrinth):
        self.labyrinth = labyrinth
        self.__visited = set()

    def find_path(self,  start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
        print(start, end, self.__visited)
        self.__visited.add(start)
        if start == end:
            print(f'Path: {[start]}')
            return [start]
        for neighbour in self.get_free_neighbours(start):
            if neighbour not in self.__visited:
                pth = self.find_path(neighbour, end)
                if pth is not None:
                    pth = pth.insert(0, start)
                    print(f'Path: {pth}')
                    return pth
        return None

    def get_free_neighbours(self, start: tuple[int, int]) -> list[tuple[int, int]]:
        neighbours = []
        if start[0] > 0 and self.labyrinth.is_free(start[0] - 1, start[1]):
            neighbours.append((start[0] - 1, start[1]))
        if start[0] < self.labyrinth.width - 1 and self.labyrinth.is_free(start[0] + 1, start[1]):
            neighbours.append((start[0] + 1, start[1]))
        if start[1] > 0 and self.labyrinth.is_free(start[0], start[1] - 1):
            neighbours.append((start[0], start[1] - 1))
        if start[1] < self.labyrinth.height - 1 and self.labyrinth.is_free(start[0], start[1] + 1):
            neighbours.append((start[0], start[1] + 1))
        return neighbours

if __name__ == '__main__':
    # lab = Labyrinth(10,10)
    # print(lab)
    # lab.save('labyrinth01.txt')
    lab = Labyrinth()
    lab.load('labyrinth01.txt')
    print(lab)
    find_path = FindPath(lab)
    # cell = (4,4)
    # print(f'Free neighbours of {cell} are: {find_path.get_free_neighbours(cell)}')
    path = find_path.find_path((0, 0), (lab.width - 1, lab.height - 1))
    print(path)