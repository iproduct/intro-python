def knapsack(W, weights, values, n):
    # Initialize DP table with zeros
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Max of (including the item, excluding the item)
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Item too heavy, exclude it
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Example Usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(capacity, weights, values, len(values)))  # Output: 220
