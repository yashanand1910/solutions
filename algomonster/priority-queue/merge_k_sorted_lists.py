from heapq import heappop, heappush
from typing import List

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    indices = [0] * len(lists)
    pq = []
    for i in range(len(lists)):
        heappush(pq, (lists[i][0], i))
    res = []
    
    while pq:
        smallest, i = heappop(pq)
        res.append(smallest)
        indices[i] += 1
        if indices[i] < len(lists[i]): heappush(pq, (lists[i][indices[i]], i))

    return res

if __name__ == '__main__':
    lists = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_k_sorted_lists(lists)
    print(' '.join(map(str, res)))

