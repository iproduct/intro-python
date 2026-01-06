import random

def longest_incr_subsequence(nums):
    n = len(nums)
    if n == 0:
        return 0
    #Initialize a dynamic list dp with length n
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    print(dp)
    # Return length of longest increasing subsequence for nums
    return max(dp)

if __name__ == '__main__':
    nums = [random.randint(1, 100) for _ in range(10)]
    # nums = [63, 2, 82, 3, 89, 44, 31, 79, 49, 49]
    print(nums)
    dp = longest_incr_subsequence(nums)
    print(dp)