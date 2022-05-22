from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while right > left:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        if sum > target:
            right -= 1
        else:
            left += 1
    return []

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum_sorted(arr, target)
    print(' '.join(map(str, res)))

