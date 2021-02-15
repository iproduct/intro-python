import numpy as np

def move(fr, to, towers, num_disks):
    print('move from ' + str(fr) + ' to ' + str(to))
    disk = towers[fr - 1].pop()
    towers[to - 1].append(disk)
    print_hanoy_towers(towers, num_disks)
    input("Hit <Enter> for next move")

def Towers(n, fr, to, spare, towers, num_disks):
    if n == 1:
        move(fr, to, towers, num_disks)
    else:
        Towers(n-1, fr, spare, to, towers, num_disks)
        Towers(1, fr, to, spare, towers, num_disks)
        Towers(n-1, spare, to, fr, towers, num_disks)

def print_hanoy_towers(towers, n):
    buffer = np.zeros([n,70])
    buffer.fill(ord(' '))
    # print(buffer.shape)
    # print(buffer)
    for tower_num in range(len(towers)):
        diskn = 0
        xcenter = tower_num * 20 + 10
        for disk in towers[tower_num]:
            pos = xcenter - disk
            while pos < xcenter + disk + 1:
                # print(pos, diskn)
                buffer[diskn][pos] = ord(str(disk))
                pos += 1
            diskn += 1
        for level in range(n):
            buffer[level][xcenter] = ord('|')

    # print(buffer)
    for y in range(n-1, -1, -1):
        for x in range(60):
            print(chr(int(buffer[y][x])), sep='', end='')
        print()

if __name__ == "__main__":
    num_disks = 4
    towers = [[disk for disk in range(num_disks, 0, -1)], [], []]
    Towers(num_disks, 1, 3, 2, towers, num_disks)

