from typing import List

def longest_sub_len(nums: List[int]) -> int:
    if not nums: return 0
    n = len(nums)
    dp = [1 for _ in range(n)]

    max_length = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                max_length = max(max_length, dp[i])

    return max_length

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = longest_sub_len(nums)
    print(res)

