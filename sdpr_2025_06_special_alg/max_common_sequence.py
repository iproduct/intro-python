def lcs(str_x, str_y):
    lenX = len(str_x)
    lenY = len(str_y)
    print(f'lenX:{lenX}, lenY:{lenY}')
    L = [[0] * (lenX + 1) for i in range(lenY + 1)]
    for i in range(lenY):
        for j in range(lenX):
            if str_x[j] == str_y[i]:
                L[i+1][j+1] = 1 + L[i][j]
            else:
                L[i+1][j+1] = max(L[i][j + 1], L[i + 1][j])
    return L

def LCS(str_x, str_y, L):
    j, i = len(str_x), len(str_y)
    solution = []
    while L[i][j] > 0:
        # print(f'X[{j-1}] = {str_x[j-1]}, Y[{i-1}] = {str_y[i-1]}, solution: {solution}')
        if str_x[j - 1] == str_y[i - 1]:
            solution.append(str_x[j - 1])
            i -= 1
            j -= 1
        elif L[i -1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(solution))

def print_matrix(L):
    for j in range(len(L[0])):
        for i in range(len(L)):
            print(L[i][j], end=' ')
        print()

if __name__ == '__main__':
    L = lcs('GTTCCTAATA', 'CGATAATTGAGA')
    print_matrix(L)
    solution = LCS('GTTCCTAATA', 'CGATAATTGAGA', L)
    print('LCS: ', solution)