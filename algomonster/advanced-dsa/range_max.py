from typing import List

class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (4 * n)
        for i in range(n):
            self.update(1, 0, n - 1, i, arr[i])

    def update(self, cur, left, right, i, val):
        if left == right and i == left:
            self.tree[cur] = val
        else:
            mid = (left + right) // 2
            if i <= mid:
                self.update(cur*2, left, mid, i, val)
            else:
                self.update(1 + (cur*2), mid + 1, right, i, val)
            self.tree[cur] = max(self.tree[2*cur], self.tree[1 + (2*cur)])

    def query(self, cur, left, right, x, y):
        if left == x and right == y:
            return self.tree[cur]
        mid = (left + right) // 2
        if x > mid:
            return self.query(1 + (2*cur), mid + 1, right, x, y)
        else:
            if y <= mid:
                return self.query(2*cur, left, mid, x, y)
            return max(self.query(2*cur, left, mid, x, mid), self.query(1 + (2*cur), mid + 1, right, mid + 1, y))

def range_max(arr: List[int], operations: List[List[int]]) -> List[int]:
    res = []
    st = SegmentTree(arr)
    for operation, *data in operations:
        if operation == 1:
            res.append(st.query(1, 0, len(arr)-1, *data))
        elif operation == 2:
            st.update(1, 0, len(arr)-1, *data)
    return res

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    operations = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = range_max(arr, operations)
    print(' '.join(map(str, res)))

