def draw(discs):
    n = len(discs[0]) + len(discs[1]) + len(discs[2])
    width = 6 * n + 9
    height = n
    buf = [[' ' for j in range(width)] for i in range(height)]
    #draw table
    buf.append('_' * width)

    #draw pivots
    for i in range(3):
        col = i * (2 * n + 3) + n
        for row in range(height):
            buf[row][col] = '|'

    # draw disks
    for i in range(3):
        num_disks = len(discs[i])
        for j in range(num_disks):
            row = height - 1 - j
            size = discs[i][j]
            pivot_col = i * (2 * n + 3) + n
            for k in range(size):
                col1 = pivot_col - k - 1
                col2 = pivot_col + k + 1
                buf[row][col1] = 'O'
                buf[row][col2] = 'O'

    # draw buffer
    for row in buf:
        print(''.join(row))

def init_discs(n):
    return[[i for i in range(n, 0, -1)], [], []]

def move(discs, frm, to):
    disc = discs[frm].pop()
    discs[to].append(disc)
    draw(discs)
    input('Hit <Enter> to continue')

def solve(discs, n, frm, to):
    other = 3 - frm - to
    if n == 1:
        move(discs, frm, to)
    else:
        solve(discs, n - 1, frm, other)
        move(discs, frm, to)
        solve(discs, n - 1, other, to)

if __name__ == '__main__':
    n = int(input("Number of discs: "))
    discs = init_discs(n)
    draw(discs)
    input('Hit <Enter> to continue')
    solve(discs, n, 0, 2)

