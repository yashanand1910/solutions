from collections import deque
from typing import List

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    queue = deque()
    res = []
    for i, num in enumerate(nums):
        while queue and nums[queue[-1]] < num:
            queue.pop()
        queue.append(i)
        if queue[0] == i - k:
            queue.popleft()
        if i >= k - 1:
            res.append(nums[queue[0]])
    return res

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = sliding_window_maximum(nums, k)
    print(' '.join(map(str, res)))

