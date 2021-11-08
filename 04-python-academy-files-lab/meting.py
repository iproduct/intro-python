def load_data(filename):
    with open(filename, encoding="utf-8") as f:
        # for line in f:
        desk = []
        line = f.readline()
        num = int(line.strip())
        line = f.readline()
        while line:
            desk.append(list(line.strip()))
            line = f.readline()
    return desk

def print_desk(desk):
    for line in desk:
        print(" ".join(line))

def melted_neighbours(desk, x, y):
    result = 0
    result += 1 if x > 0 and desk[x-1][y] == "0" else 0
    result += 1 if x < len(desk) - 1 and desk[x+1][y] == "0" else 0
    result += 1 if y > 0 and desk[x][y-1] == "0" else 0
    result += 1 if y < len(desk) - 1 and desk[x][y+1] == "0" else 0
    return result


def melting_step(desk):
    n = len(desk)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if desk[i][j] == "*" and melted_neighbours(desk, i, j) >= 2:
                desk[i][j] = "1"
            j += 1
        i += 1

    unmelted = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            if desk[i][j] == "1":
                desk[i][j] ="0"
            elif desk[i][j] == "*":
                unmelted += 1
            j += 1
        i += 1
    return unmelted

if __name__ == "__main__":
    desk = load_data("melting_data.txt")
    print_desk(desk)
    hours = 0
    while melting_step(desk) > 0:
        print()
        print_desk(desk)
        hours += 1
    print()
    print_desk(desk)
    hours += 1
    print("Number of hours:", hours)
