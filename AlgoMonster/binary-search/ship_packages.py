from typing import List

def is_feasible(weights: List[int], max_weight: int, d: int) -> bool:
    capacity = max_weight
    days = 1
    i = 0
    
    while i < len(weights):
        if capacity >= weights[i]:
            capacity -= weights[i]
            i += 1
        else:
            days += 1
            capacity = max_weight
    
    return days <= d
        

def min_max_weight(weights: List[int], d: int) -> int:
    left, right = max(weights), sum(weights)
    index = right
    
    while left <= right:
        mid = (left + right) // 2
        if is_feasible(weights, mid, d):
            index = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return index

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)
