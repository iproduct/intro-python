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


def knapsack_1d(W, weights, values, n):
    # Create a 1D array of size W + 1 initialized to 0
    dp = [0] * (W + 1)

    for i in range(n):
        # Iterate backwards to ensure each item is used only once
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[W]


def knapsack_backtracking(index, current_weight, current_profit):
    global max_profit

    # Base case: reached end of items
    if index == n:
        if current_profit > max_profit:
            max_profit = current_profit
        return

    # Option 1: Include item (if it fits)
    if current_weight + weights[index] <= capacity:
        knapsack_backtracking(index + 1, current_weight + weights[index], current_profit + values[index])

    # Option 2: Exclude item
    knapsack_backtracking(index + 1, current_weight, current_profit)


# Initialize variables
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
max_profit = 0

knapsack_backtracking(0, 0, 0)
print(max_profit)
