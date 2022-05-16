from typing import List

def is_time_feasible(newspapers: List[int], coworkers: int, t: int) -> bool:
    total_time = t
    i = 0
    workers_allocated = 1
    
    while i < len(newspapers):
        if newspapers[i] <= total_time:
            total_time -= newspapers[i]
            i += 1
        else:
            workers_allocated += 1
            total_time = t
            
    return workers_allocated <= coworkers

def newspapers_split(newspapers: List[int], coworkers: int) -> int:
    left, right = max(newspapers), sum(newspapers)
    boundary_index = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_time_feasible(newspapers, coworkers, mid):
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return boundary_index

if __name__ == '__main__':
    newspapers = [int(x) for x in input().split()]
    coworkers = int(input())
    res = newspapers_split(newspapers, coworkers)
    print(res)
