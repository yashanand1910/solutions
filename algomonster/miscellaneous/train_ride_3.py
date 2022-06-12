from heapq import heappush, heappop
from typing import List

class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y
    
    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)

def train_ride_3(n: int, k: int, t: int, p: int, connections: List[List[int]], teleporters: List[List[int]]) -> int:
    graph = [[] for i in range(n + 1)]
    graph_tele = [[] for i in range(n + 1)]

    dsu = UnionFind()
    for i, j in teleporters:
        dsu.union(i, j)

    for i, j, price, time in connections:
        graph[i].append((time, j, price))
        graph[j].append((time, i, price))
        graph_tele[dsu.find(i)].append((time, dsu.find(j), price))
        graph_tele[dsu.find(j)].append((time, dsu.find(i), price))

    def time_taken(use_tele, max_price):
        if max_price < 0:
            return float('inf')
        queue = []
        min_time = [float('inf') for i in range(n + 1)]
        if use_tele:
            heappush(queue, (0, dsu.find(1), 0))
            min_time[dsu.find(1)] = 0
        else:
            heappush(queue, (0, 1, 0))
            min_time[1] = 0
        while queue:
            time, cur, price = heappop(queue)
            if cur == (dsu.find(n) if use_tele else n):
                break
            if min_time[cur] < time:
                continue
            for n_time, n_cur, n_price in (graph_tele[cur] if use_tele else graph[cur]):
                if n_price > max_price:
                    continue
                total_time = time + n_time
                if total_time < min_time[n_cur]:
                    min_time[n_cur] = total_time
                    heappush(queue, (total_time, n_cur, n_price))
        return (min_time[n] if not use_tele else min_time[dsu.find(n)])

    left, right = 1, k
    min_price = -1
    while left <= right:
        mid = (left + right) // 2
        if time_taken(False, mid) <= t or time_taken(True, mid - p) <= t:
            min_price = mid
            right = mid - 1
        else:
            left = mid + 1
    return min_price

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    t = int(input())
    p = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    teleporters = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride_3(n, k, t, p, connections, teleporters)
    print(res)

