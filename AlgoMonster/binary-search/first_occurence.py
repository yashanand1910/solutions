from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    index = -1
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            if arr[mid] == target: index = mid
            right = mid - 1
            
    return index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
