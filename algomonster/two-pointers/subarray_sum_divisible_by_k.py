from typing import List

def subarray_sum_divisible(nums: List[int], k: int) -> int:
    prefix_rem = {0: 1}
    cur_sum = 0
    n = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        rem = cur_sum % k
        if rem in prefix_rem:
            n += prefix_rem[rem]
        if rem in prefix_rem:
            prefix_rem[rem] += 1
        else:
            prefix_rem[rem] = 1
    return n

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = subarray_sum_divisible(nums, k)
    print(res)

