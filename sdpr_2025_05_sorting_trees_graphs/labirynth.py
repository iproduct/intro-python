from collections import deque


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'

class Labirynth:
    def __init__(self, size: int, blocked_list_x_y_tuples):
        self.size = size
        self.cells = {}
        self.blocked_set = set(blocked_list_x_y_tuples)
        for i in range(size):
            for j in range(size):
                if not (i,j) in self.blocked_set: # O(1)
                    self.cells[(i,j)] = Cell(i, j)
        for i in range(size):
            for j in range(size):
                if not (i, j) in self.blocked_set:
                    print((i,j), self._get_neighbours_x_y_tuples(i,j))
                    self.cells[(i,j)].neighbors = [self.cells[x_y_tuple] for x_y_tuple in self._get_neighbours_x_y_tuples(i,j)]

    def _get_neighbours_x_y_tuples(self, x, y):
        neighbours = []
        if x - 1 >= 0 and not (x-1, y) in self.blocked_set:
            neighbours.append((x-1, y))
        if x + 1 < self.size and not (x+1, y) in self.blocked_set:
            neighbours.append((x+1, y))
        if y - 1 >= 0 and not (x, y-1) in self.blocked_set:
            neighbours.append((x, y-1))
        if y + 1 < self.size  and not (x, y+1) in self.blocked_set:
            neighbours.append((x, y + 1))
        return neighbours

    def find_shortest_path_bfs(self, start_x_y_tuple, target_x_y_tuple):
        paths_queue = deque()
        paths_queue.append([start_x_y_tuple])
        visited_x_y_tuples = set() # O(1)
        visited_x_y_tuples.add(start_x_y_tuple)
        while paths_queue:
            current_path = paths_queue.popleft()
            print(current_path)
            current_x_y_tuple = current_path[-1]
            if current_x_y_tuple == target_x_y_tuple:
                return current_path
            for neighbor in self.cells[current_x_y_tuple].neighbors:
                neighbor_x_y_tuple = (neighbor.x, neighbor.y)
                if  neighbor_x_y_tuple not in visited_x_y_tuples:
                    visited_x_y_tuples.add( neighbor_x_y_tuple)
                    paths_queue.append(current_path + [neighbor_x_y_tuple])
        return None

if __name__ == '__main__':
    lab = Labirynth(5, [(0, 1), (1, 1), (2, 1), (1,3), (2,3), (3,3)])
    print('Shortest path:', lab.find_shortest_path_bfs((0, 0), (3, 4)))




