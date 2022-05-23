from typing import List

def subarray_sum_total(arr: List[int], target: int) -> int:
    prefix_sum = {0: [-1]}
    cur_sum = 0
    n = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum - target in prefix_sum:
            n += len(prefix_sum[cur_sum - target])
        if cur_sum in prefix_sum:
            prefix_sum[cur_sum].append(i)
        else:
            prefix_sum[cur_sum] = [i]
    return n

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_total(arr, target)
    print(res)

