from heapq import heappush, heappop
from typing import List

def time_taken(graph, z):
    queue = []
    heappush(queue, (0, 1, 0))
    dist = [float('inf') for i in range(len(graph))]
    dist[0] = 0
    while queue:
        distance, cur, line = heappop(queue)
        if distance > dist[cur - 1]:
            continue
        if cur == n:
            break
        for d, i, l in graph[cur - 1]:
            if l > z:
                continue
            new_d = d + distance
            if dist[i - 1] > new_d:
                heappush(queue, (new_d, i, l))
                dist[i - 1] = new_d
    return dist[n - 1]

def train_ride_2(n: int, k: int, t: int, connections: List[List[int]]) -> int:
    graph = [[] for i in range(n)]
    for i, j, line, dist in connections:
        graph[i - 1].append((dist, j, line))
        graph[j - 1].append((dist, i, line))

    left, right = 1, k
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        time = time_taken(graph, mid)
        if time > t:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    return ans

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    t = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride_2(n, k, t, connections)
    print(res)

