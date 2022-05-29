from functools import lru_cache
from typing import List

def can_partition(nums: List[int]) -> bool:
    target = sum(nums) // 2
    if sum(nums) % 2 != 0 or max(nums) > target:
        return False

    used = []

    @lru_cache(None)
    def dfs(target):
        if target == 0:
            return True
        if target < 0:
            return False
        for i in nums:
            if i in used:
                continue
            used.append(i)
            ans = dfs(target - i)
            if ans:
                return True
            used.pop()
        return False

    return dfs(target)

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print('true' if res else 'false')

