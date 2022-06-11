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

def train_ride(n: int, k: int, connections: List[List[int]]) -> int:
    dsu = UnionFind()
    lines = [[] for i in range(k)]
    for i, j, line in connections:
        lines[line - 1].append([i, j])

    for line_no, line in enumerate(lines):
        for i, j in line:
            dsu.union(i, j)
        if dsu.find(1) == dsu.find(n):
            return line_no + 1

    return -1

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride(n, k, connections)
    print(res)

