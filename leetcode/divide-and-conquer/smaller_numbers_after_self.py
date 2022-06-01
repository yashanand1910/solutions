from typing import List

def count_smaller(nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 1: return [0]
    if n == 0: return []

    mid = n // 2
    l_res = count_smaller(nums[:mid])
    r_res = count_smaller(nums[mid:])

    # merge both results
    for i in range(len(l_res)):
        for j in range(len(r_res)):
            if nums[mid + j] < nums[i]:
                l_res[i] += 1
    for i in r_res:
        l_res.append(i)

    return l_res

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = count_smaller(nums)
    print(' '.join(map(str, res)))

