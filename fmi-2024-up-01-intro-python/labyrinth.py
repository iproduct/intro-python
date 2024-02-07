
lab = (
    (0, 0, 0, 1, 0, 1),
    (1, 0, 0, 1, 0, 0),
    (0, 1, 0, 1, 0, 1),
    (0, 0, 0, 1, 0, 1),
    (1, 0, 1, 1, 0, 1),
    (0, 0, 0, 0, 0, 1),
)

start =(0, 0)
goal = (5, 1)


def find_neighbours(start, lab):
    x, y = start
    results = []
    lenY = len(lab)
    lenX = len(lab[0])
    if x > 1 and lab[y][x-1] == 0:
       results.append((x-1, y))
    if x < lenX-1 and lab[y][x+1] == 0:
       results.append((x+1, y))
    if y > 1 and lab[y-1][x] == 0:
       results.append((x, y-1))
    if y < lenY-1 and lab[y+1][x] == 0:
       results.append((x, y + 1))
    return results

def find_path(start, goal, lab, visited):
    if start == goal:
        return [goal]
    neighbours = find_neighbours(start, lab)
    for neighbour in neighbours:
        if neighbour in visited:
            continue
        visited.append(neighbour)
        path = find_path(neighbour, goal, lab, visited)
        if path is not None:
            return [start].extend(path)
    return None
if __name__ == "__main__":
    n = find_neighbours((2,3), lab)
    path = find_path(start, goal, lab, [])
    print(path)
