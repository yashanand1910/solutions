from typing import List

def subarray_sum(arr: List[int], target: int) -> List[int]:
    prefix_sum = {0 : -1}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        prefix_sum[cur_sum] = i
        if cur_sum - target in prefix_sum:
            return [prefix_sum[cur_sum - target] + 1, i  + 1]
    return []

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum(arr, target)
    print(' '.join(map(str, res)))

