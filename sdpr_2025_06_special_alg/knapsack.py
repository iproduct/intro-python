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




def knapsack_backtracking(capacity, weights, profits):
    max_profit = 0

    def knapsack_backtrack(index, current_weight, current_profit):
        nonlocal max_profit
        n = len(values)

        # Base case: reached end of items
        if index == n:
            if current_profit > max_profit:
                max_profit = current_profit
            return

        # Option 1: Include item (if it fits)
        if current_weight + weights[index] <= capacity:
            knapsack_backtrack(index + 1, current_weight + weights[index], current_profit + profits[index])

        # Option 2: Exclude item
        knapsack_backtrack(index + 1, current_weight, current_profit)

    knapsack_backtrack(0,0,0)
    return max_profit

if __name__ == '__main__':
    # Example Usage
    # values = [60, 100, 120]
    # weights = [10, 20, 30]
    # capacity = 50
    # Output: 220
    values = [1,2,3]
    weights = [4,5,1]
    capacity = 4

    print(knapsack_backtracking(capacity, weights, values))
