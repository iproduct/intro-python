
lab = (
    (0, 0, 0, 1, 0, 1)
    (1, 0, 0, 1, 0, 0)
    (0, 1, 0, 1, 0, 1)
    (0, 0, 0, 1, 0, 1)
    (1, 0, 1, 1, 0, 1)
    (0, 0, 0, 0, 0, 1)
)

start =(1, 1)
goal = (6, 2)


def find_neighbours(start, lab):
    x, y = start
    results = []
    lenY = len(lab)
    lenX = len(lab(0))
    if x > 1 and lab[y-1, x-2] == 0:
       results.append((x-1, y))
    if x < lenX and lab[y-1, x] == 0:
       results.append((x+1, y))
    if y > 1 and lab[y-2, x-1]:
       results.append((x, y-1))
    if y < lenY and lab[y, x-1]:
       results.append((x, y + 1))
    return results

def find_path(start, goal):
    if start == goal:
        return [goal]
    neighbours = find_neighbours(start)