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

def umbristan(n: int, breaks: List[List[int]]) -> List[int]:
    length = len(breaks)
    res = [0] * length
    res[-1] = n
    dsu = UnionFind()

    for i in range(length - 1, 0, -1):
        if dsu.find(breaks[i][0]) != dsu.find(breaks[i][1]):
            res[i - 1] = res[i] - 1
        else:
            res[i - 1] = res[i]
        dsu.union(breaks[i][0], breaks[i][1])

    return res

if __name__ == '__main__':
    n = int(input())
    breaks = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = umbristan(n, breaks)
    print(' '.join(map(str, res)))

