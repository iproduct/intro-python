def printMove(fromP, toP):
    print('move from ' + str(fromP) + ' to ' + str(toP))


def Towers(n, fromP, toP, spareP):
    if n == 1:
        printMove(fromP, toP)
    else:
        Towers(n - 1, fromP, spareP, toP)
        Towers(1, fromP, toP, spareP)
        Towers(n - 1, spareP, toP, fromP)

if __name__ == "__main__":
    n = int(input('N = '))
    Towers(n, 1, 3, 2)