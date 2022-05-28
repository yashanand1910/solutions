from typing import List

def find_largest_subset(nums: List[int]) -> int:
    if not nums: return 0
    nums.sort()
    n = len(nums)
    dp = [1 for _ in range(n)]

    max_set = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], 1 + dp[j])
        max_set = max(max_set, dp[i])

    return max_set

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = find_largest_subset(nums)
    print(res)

