from heapq import heappop, heappush
from typing import List

def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    pq = []
    for i, j in points:
        x = tuple([i**2 + j**2, [i, j]])
        heappush(pq, x)
    res = []
    for _ in range(k):
        res.append(heappop(pq)[1])

    return res

if __name__ == '__main__':
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = k_closest_points(points, k)
    for row in res:
        print(' '.join(map(str, row)))

