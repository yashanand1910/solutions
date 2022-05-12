from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)-1
    index = len(arr)-1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            index = mid
            right = mid - 1
    return index   

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
