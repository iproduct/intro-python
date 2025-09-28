if __name__ == "__main__":
    # a2 = [[0]*10]*5
    a2 = [[0] * 10 for i in range(5)]
    a2[0][0] = 1
    for i in range(len(a2)):
        print(a2[i])

    a3 = list(range(3))
    for i in range(len(a3)):
        a3[i] = list(range(4))
        for j in range(len(a3[0])):
            a3[i][j] = list(range(5))
            for k in range(len(a3[0][0])):
                a3[i][j][k] = i + j + k
    for i in range(len(a3)):
        for j in range(len(a3[0])):
            print(a3[i][j])
        print()