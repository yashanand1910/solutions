from typing import List

def min_subarrays(mid, nums):
    cur_sum = 0
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] > mid:
            return float('inf')
        if (cur_sum + nums[i]) > mid:
            count += 1
            cur_sum = 0
        cur_sum += nums[i]
        i += 1
    return count + 1

def split_array_largest_sum(nums: List[int], m: int) -> int:
    left, right = 0, sum(nums)

    while left < right:
        mid = (left + right) // 2
        if min_subarrays(mid, nums) > m:
            left = mid + 1 
        else:
            right = mid

    return right

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    m = int(input())
    res = split_array_largest_sum(nums, m)
    print(res)

