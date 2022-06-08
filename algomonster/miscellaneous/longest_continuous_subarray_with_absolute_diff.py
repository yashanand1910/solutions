from collections import deque
from typing import List

def longest_subarray(nums: List[int], limit: int) -> int:
    q_min = deque()
    q_max = deque()
    left, right = 0, 0
    max_length = 0
    while right < len(nums):
        while q_min and nums[q_min[-1]] > nums[right]:
            q_min.pop()
        q_min.append(right)
        while q_max and nums[q_max[-1]] < nums[right]:
            q_max.pop()
        q_max.append(right)
        while left < right and nums[q_max[0]] - nums[q_min[0]] > limit:
            if q_max[0] == left: q_max.popleft()
            if q_min[0] == left: q_min.popleft()
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length
    
if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    limit = int(input())
    res = longest_subarray(nums, limit)
    print(res)

