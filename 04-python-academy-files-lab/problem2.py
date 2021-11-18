import sys

command = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

def translate(x):
    return command[x]

def find_max_path_from(table, i, j):
    steps = 0
    visited = set()  # in O(1)
    while True:
        visited.add((i, j))
        steps += 1
        dir_r, dir_c = table[i][j]
        i += dir_r
        j += dir_c
        if i < 0 or i >= len(table) or j < 0 or j >= len(table[0]) or (i, j) in visited:
            return steps
    return steps

def print_tuple(solution):
    return "{} {} {}".format(*solution)

def find_max_path(table):
    max = -1
    max_solutions = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            steps = find_max_path_from(table, i, j)
            if steps == max:
                max_solutions.append((i+1, j+1, steps))
            elif steps > max:
                max = steps
                max_solutions = [(i+1, j+1, steps)]
    return ";".join(map(print_tuple, max_solutions))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: problem2.py <test_file_name>")
        exit(0)
    with open(sys.argv[1], "r") as f:
        num_tests = int(f.readline().strip())
        for _ in range(num_tests):
            f.readline()
            rows, cols = map(int, f.readline().strip().split(" "))
            table = []
            for _ in range(rows):
                line = list(f.readline().strip())
                table.append(list(map( translate, line)))
            print(find_max_path(table))