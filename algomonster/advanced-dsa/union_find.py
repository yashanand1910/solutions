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

class SameSet:
    def __init__(self):
        self.u = UnionFind()

    def merge(self, x: int, y: int) -> None:
        self.u.union(x, y)

    def is_same(self, x: int, y: int) -> bool:
        return self.u.find(x) == self.u.find(y)

if __name__ == '__main__':
    sol = SameSet()
    for _ in range(int(input())):
        op, *args = input().split()
        x, y = map(int, args)
        if op == 'union':
            sol.merge(x, y)
        elif op == 'is_same':
            res = sol.is_same(x, y)
            print('true' if res else 'false')

