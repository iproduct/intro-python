def square(x, y):
    return x*y

nbs = [(-1,0), (1, 0), (0, -1), (0, 1)]
def count_zeros(m, i, j):
    zeros = 0
    for nb in nbs:
        r = i + nb[0]
        c = j + nb[1]
        if r < 0 or r >= len(m) or c < 0 or c >= len(m[0]):
            continue
        zeros += m[r][c] == '0'
    return zeros

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
        