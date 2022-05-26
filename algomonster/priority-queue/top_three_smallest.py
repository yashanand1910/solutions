from heapq import heapify, heappop
from typing import List

def heap_top_3(arr: List[int]) -> List[int]:
    heapify(arr)
    res = []
    for i in range(3): res.append(heappop(arr))
    return res

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = heap_top_3(arr)
    print(' '.join(map(str, res)))

