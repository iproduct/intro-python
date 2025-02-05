from labirynth import print_labyrinth

def read_labyrinth(filename: str) -> list[list[int]]:
    labyrinth = []
    # f = open(filename, 'rt')
    with open(filename, 'rt') as f:
        lines = f.readlines()
        rows, cols = lines[0].split(',')
        for row in range(1, int(rows) + 1):
            cells = lines[row].split(',')
            lab_row = []
            for cell in cells:
                lab_row.append(int(cell))
            labyrinth.append(lab_row)
    return labyrinth


if __name__ == "__main__":
    labyrinth = read_labyrinth('labyrinth.txt')
    print_labyrinth(labyrinth)