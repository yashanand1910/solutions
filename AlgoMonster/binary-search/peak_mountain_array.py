from typing import List

# considering plateaus exist. if peak is plateau, then finds first index
def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr)-1
    peak = 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        elif arr[mid] >= arr[mid+1]:
            peak = mid
            right = mid - 1
        else:
            peak = mid
            i = mid
            while arr[i] != arr[mid]: i += 1
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            elif arr[mid] > arr[mid+1]:
                right = mid - 1
            
    return peak 
            

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
