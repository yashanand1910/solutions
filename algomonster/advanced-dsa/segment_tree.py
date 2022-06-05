from typing import List

class SegmentTree:
    def __init__(self, arr: List[int]):
        self.tree = [0] * len(arr)
        sums = []
        for i in range(len(arr)):

    # def sum(self, i, j):
    #     # TODO
    
    # def set(self, i, val):
    #     # TODO

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

