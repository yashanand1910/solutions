from typing import List

def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr)-1
    index = 0
    
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            index = mid
            right = mid - 1
            
    return index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
