def draw(d1, d2, d3):
    n = len(d1) + len(d2) + len(d3)
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
    discs = (d1, d2, d3)
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

if __name__ == '__main__':
    draw([5,4,3,2,1], [], [])
