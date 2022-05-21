from typing import List

class UnionFind:
    def __init__(self):
        self.f = {}
    def find(self, x):
        y = self.f.get(x, x)
        if y != x:
            return self.find(y)
        return x
    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)

def mst_forest(trees: int, pairs: List[List[int]]) -> int:
    edges = sorted(pairs, key=lambda edge: edge[2])
    dsu = UnionFind()
    res, n = 0, 0
    for edge in edges:
        if dsu.find(edge[0]) != dsu.find(edge[1]):
            dsu.union(edge[0], edge[1])
            n += 1
            res += edge[2]
            if n == trees - 1:
                break
    return res

if __name__ == '__main__':
    trees = int(input())
    pairs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = mst_forest(trees, pairs)
    print(res)

