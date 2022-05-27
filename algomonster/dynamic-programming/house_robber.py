from typing import List

def rob(nums: List[int]) -> int:
    def foo(n, dp):
        if n in dp: return dp[n]        
        if n + 1 not in dp:
            dp[n + 1] = foo(n + 1, dp)
        if n + 2 not in dp:
            dp[n + 2] = foo(n + 2, dp)
        return max(nums[n] + dp[n + 2], dp[n + 1])

    dp = {len(nums): 0, len(nums)-1: nums[-1], len(nums) + 1: 0}
    return foo(0, dp)

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = rob(nums)
    print(res)

