def lcs(strX, strY):
    lenX = len(strX)
    lenY = len(strY)
    row = [0] * (lenX + 1)
    L = [[0] * (lenX + 1) for i in range(lenY + 1)]
    for i in range(lenY):
        for j in range(lenX):
            if strX[j] == strY[i]:
                L[i+1][j+1] = 1 + L[i][j]
            else:
                L[i+1][j+1] = max(L[i][j + 1], L[i + 1][j])
    print_matrix(L)

def print_matrix(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            print(L[i][j], end=' ')
        print()

if __name__ == '__main__':
    lcs('GTTATAAATGACA', 'AGAAATCTA')