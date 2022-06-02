class UnionFind:
    def __init__(self):
        self.id = {}
        self.count = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.count[self.find(y)] = self.get_count(self.find(x)) + self.get_count(self.find(y))
        self.id[self.find(x)] = self.find(y)

    def get_count(self, x):
        return self.count.get(self.find(x), 1)

class SetCounter:
    def __init__(self):
        self.dsu = UnionFind()

    def merge(self, x: int, y: int) -> None:
        self.dsu.union(x, y)

    def count(self, x: int) -> int:
        return self.dsu.get_count(x)

if __name__ == '__main__':
    sol = SetCounter()
    for _ in range(int(input())):
        op, *args = input().split()
        if op == 'union':
            [x, y] = map(int, args)
            sol.merge(x, y)
        elif op == 'count':
            [x] = map(int, args)
            res = sol.count(x)
            print(res)

