from typing import List

def binary_search(arr: List[int], target: int) -> int:
    pivot = len(arr)//2
    if arr[pivot] == target: return pivot
    elif pivot == 0 and arr[pivot] != target: return -1
    if target < arr[pivot]: return binary_search(arr[:pivot], target)
    else: return pivot + binary_search(arr[pivot:], target)

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
