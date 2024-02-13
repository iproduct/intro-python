from functools import reduce


def square(x, y):
    return x*y

nbs = [(-1,0), (1, 0), (0, -1), (0, 1)]
def count_zeros(m, i, j):
    zeros = 0
    if m[i][j] == '0':
        return 5
    for nb in nbs:
        r = i + nb[0]
        c = j + nb[1]
        if r < 0 or r >= len(m) or c < 0 or c >= len(m[0]):
            continue
        zeros += m[r][c] == '0'
    return zeros

def transform(matrix):
    neighbours = [[count_zeros(matrix, r, c) for c, _ in enumerate(row)] for r, row in enumerate(matrix)]
    return list(map(lambda row: list(map(lambda col: '0' if col >= 2 else '*', row)), neighbours))

def print_matrix(m):
    print()
    for row in m:
        print(row)


if __name__ == '__main__':
    m = map(square, range(1, 11), range(6,1,-1))
    print(list(m))

    l=['00000000', '00**0000', '00**0**0', '0******0', '0*****00', '0**0**00', '00000000', '00000000']

    rows = map(lambda row: '*' if '*' in row else '0', l)
    print(list(rows), '\n')

    m = [list(row) for row in l]
    for line in m:
        print(line)

    print()
    neighbours = [[count_zeros(m, r, c) for c in range(len(m[0]))] for r in range(len(m))]
    for line in list(neighbours):
        print(line)

    print()
    new_m =map(lambda row: (map(lambda col: '0' if col >= 2 else '*', row)), neighbours)
    for line in new_m:
        for cell in line:
            print(cell, end=' ')
        print()

    # Solving original 'iseberg melting' problem
    matrix = m
    print_matrix(matrix)
    steps = 0
    while reduce(lambda acc, row: acc or any(col == '*' for col in row), matrix, False):
        input("[ENTER] for next step:")
        matrix = transform(matrix)
        steps += 1
        print_matrix(matrix)
    print(f'Isberg melted for {steps} hours.')