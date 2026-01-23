
def load_from_file(filename):
    with open(filename, 'r') as f:
        rows, cols = f.readline().strip().split()
        labyrinth = []
        for line in f:
            labyrinth.append(line.strip())
    if len(labyrinth) != int(rows) or len(labyrinth[0]) != int(cols):
        raise IOError(f'File does not have the correct format: {rows} x {cols}, '
                      f'but is: {len(labyrinth)} x {len(labyrinth[0])}')
    return labyrinth

def print_labyrinth(labyrinth):
    for row in labyrinth:
        print(row)

if __name__ == "__main__":
    labyrinth = load_from_file('labyrinth.txt')
    print_labyrinth(labyrinth)
