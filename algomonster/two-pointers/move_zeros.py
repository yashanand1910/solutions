from typing import List

def move_zeros(nums: List[int]) -> None:
    slow, fast = 0, 0
    while fast < len(nums):
        if nums[slow] != 0 and nums[fast] != 0:
            fast += 1
            continue
        if nums[slow] != 0:
            slow = fast
        if nums[fast] == 0:
            fast += 1
            continue
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))

