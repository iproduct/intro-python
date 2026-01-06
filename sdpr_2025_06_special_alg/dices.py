def dices_cout_ways(m, n, X):
    # Initialize 3-dim dp list: n x X
    dp = [[0] * (X+1) for i in range(n + 1)]

    # Initilize base case one dice
    for i in range(1, min(m, X) + 1):
        dp[1][i] = 1

    # Walking the number of dices as i
    for i in range(2, n + 1):
        # Walking the sum X as j
        for j in range(1, X + 1):
            # Walking the dice draw as k
            for k in range(1, m + 1):
                if  j >= k:
                    dp[i][j]  += dp[i - 1][j-k]

    # Return dp for original sum X with n dices
    return dp[n][X]

if __name__ == '__main__':
    print(dices_cout_ways(2, 2, 3))
    print(dices_cout_ways(6, 3, 8))
    print(dices_cout_ways(6, 3, 4))

