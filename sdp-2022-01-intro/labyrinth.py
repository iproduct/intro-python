labyrinth = [
    (0, 1, 0, 1, 1),
    (0, 1, 0, 0, 0),
    (0, 0, 0, 1, 0),
    (1, 1, 0, 1, 0),
    (0, 1, 0, 1, 0),
]


def next_move(lab, point_xy, visited):
    """
    Find next move in a labyrinth without loops
    :param lab: the labyrinth
    :param point_xy: start
    :param visited: list of visited points
    :return: path found
    """
    x, y = point_xy
    height = len(labyrinth)
    width = len(labyrinth[0])
    if x > 0 and lab[x - 1][y] == 0 and (x - 1, y) not in visited:
        return (x - 1, y)
    elif x < width - 1 and lab[x + 1][y] == 0 and (x + 1, y) not in visited:
        return (x + 1, y)
    elif y > 0 and lab[x][y - 1] == 0 and (x, y - 1) not in visited:
        return (x, y - 1)
    elif x < height - 1 and lab[x][y + 1] == 0 and (x, y + 1) not in visited:
        return (x, y + 1)
    else:
        return None


def find_path(lab, x_start, y_start, x_end, y_end):
    current = (x_start, y_start)
    current_path = [current]
    visited = [current]

    while current != (x_end, y_end):
        current = next_move(lab, current, visited)
        # backtracking - step back
        if current == None:
            current_path.pop()
            current = current_path.pop()
        current_path.append(current)
        visited.append(current)
        print(current, '->', current_path)
    result_path = []
    for point in current_path:
        y, x = point
        result_path.append((x, y))
    return result_path


if __name__ == '__main__':
    print('Path found:', find_path(labyrinth, 0, 0, 4, 4))
