import random
from cmath import inf


def longest_incr_subsequence(nums):
    def compute_dp():
        n = len(nums)
        if n == 0:
            return 0
        #Initialize a dynamic list dp with length n + 1 : [0,n]
        dp = [1] * (n + 1)
        dp[0] = 0
        for i in range(2, n + 1):
            for j in range(1, i):
                if nums[i-1] > nums[j-1] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

        print_list(dp)
        # Return length of longest increasing subsequence for nums
        return dp

    def find_min_num_with_dp_val(dp_val, right_index):
        print(dp_val, right_index, '->', end=' ')
        min_num = inf
        index_min_num = 0
        for i in range(1, right_index):
            if dp[i] == dp_val and nums[i-1] <= min_num:
                min_num = nums[i-1]
                index_min_num = i
        print(min_num, index_min_num)
        return min_num, index_min_num

    n = len(nums)
    dp = compute_dp()
    max_dp = max(dp)
    solution = []
    min_num_index_dp = n+1

    for i in range(max_dp, 0, -1):
        min_num, min_num_index_dp = find_min_num_with_dp_val(i, min_num_index_dp)
        solution.append(min_num)

    return max_dp, solution[::-1]

def print_list(l):
    for el in l:
        print(f'{el:3} ', end=" ")
    print()


# Old version:
def longest_incr_subsequence_old(nums):
    n = len(nums)
    if n == 0:
        return 0
    #Initialize a dynamic list dp with length n
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    # print(dp)
    # Return length of longest increasing subsequence for nums
    return max(dp)


if __name__ == '__main__':
    nums = [random.randint(1, 100) for _ in range(10)]
    # nums = [63, 2, 82, 3, 89, 44, 31, 79, 49, 49]
    # nums = [11, 51, 86, 79, 44, 95, 56, 79, 64, 99]
    # nums = [47, 56, 91, 52, 30, 75, 83, 44, 34, 74]
    # nums = [4, 49, 58, 23, 64, 39, 91, 12, 12, 7]
    nums2 = [' ']
    nums2.extend(nums)
    print_list(nums2)

    # New - with example solution
    max_subseq_len, solution = longest_incr_subsequence(nums)
    print('\nMax increasing sequence length:', max_subseq_len)
    print('Sample solution:', solution)

    # Old - only length of the sequence
    print('\nOld solution to compare with:', longest_incr_subsequence_old(nums))