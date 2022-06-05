from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        print(arr)
        self.n = len(arr)
        self.tree = [0] * (4 * len(arr))
        sums = [0] * len(arr)
        for i in range(self.n):
            sums[i] = int(arr[i]) + (int(sums[i-1]) if i > 0 else 0)
        
        def update(i, j, start):
            self.tree[start] = sums[j] - (sums[i-1] if i > 0 else 0)
            if i == j:
                return
            mid = (j + i + 1) // 2
            update(i, mid - 1, 2 * (start) + 1)
            update(mid, j, 2 * (start) + 2)
        
        update(0, self.n - 1, 0)

    def sum(self, i, j):
        i, j = int(i), int(j)
        def query(i, j, x, y, start):
            if i == x and j == y:
                return self.tree[start]

            mid = (x + y + 1) // 2
            if i >= mid:
                return query(i, j, mid, y, 2 * (start) + 2)
            else:
                if j < mid:
                    return query(i, j, x, mid - 1, 2 * (start) + 1)
                else:
                    return query(i, mid - 1, x, mid - 1, 2 * (start) + 1) + query(mid, j, mid, y, 2 * (start) + 2)
        return query(i, j, 0, self.n - 1, 0)
    
    def set(self, i, val):
        # TODO

if __name__ == '__main__':
    arr = input('Enter array: ').split(' ')
    st = SegmentTree(arr)
    print('Enter commands (\'end\' to end):')
    operation, *data = input().split(' ')
    while operation != 'end':
        if operation == 'sum':
            print(st.sum(*data))
        elif operation == 'set':
            st.set(*data)
        operation, *data = input().split(' ')

