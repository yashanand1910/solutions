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

def number_of_connected_components(n: int, connections: List[List[int]]) -> List[int]:
    res = [0] * len(connections)
    dsu = UnionFind()

    for i, (x, y) in enumerate(connections):
        if dsu.find(x) != dsu.find(y):
            res[i] = (res[i - 1] - 1) if i > 0 else n - 1
        else:
            res[i] = (res[i - 1]) if i > 0 else n
        dsu.union(x, y)

    return res

if __name__ == '__main__':
    n = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = number_of_connected_components(n, connections)
    print(' '.join(map(str, res)))

