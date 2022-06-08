from typing import List

def next_greater_elements(nums: List[int]) -> List[int]:
    stack = []
    n = len(nums)
    res = [-1] * n
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack[-1]] = num
            stack.pop()
        stack.append(i)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack[-1]] = num
            stack.pop()
    return res

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = next_greater_elements(nums)
    print(' '.join(map(str, res)))

