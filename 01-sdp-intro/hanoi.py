def printMove(from_tower, to_tower):
    print('move from ' + str(from_tower) + ' to ' + str(to_tower))

def Towers(n, from_tower, to_tower, spare_tower):
    if n == 1:
        printMove(from_tower, to_tower)
    else:
        Towers(n-1, from_tower, spare_tower, to_tower)
        Towers(1, from_tower, to_tower, spare_tower)
        Towers(n-1, spare_tower, to_tower, from_tower)

if __name__ == '__main__':
    Towers(4, 1, 3, 2)