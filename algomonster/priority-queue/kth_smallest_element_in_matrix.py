from heapq import heappush, heappop
from typing import List

def kth_smallest(matrix: List[List[int]], k: int) -> int:
    pq = []
    n = len(matrix)
    row_i = [0] * n
    col_i = [0] * n
    heappush(pq, (matrix[0][0], 0, 0))
    for _ in range(k - 1):
        smallest, row, col = heappop(pq)
        row_i[row] = col + 1
        col_i[col] = row + 1
        if col + 1 < n and col_i[col + 1] == row:
            heappush(pq, (matrix[row][col + 1], row, col + 1))
        if row + 1 < n and row_i[row + 1] == col:
            heappush(pq, (matrix[row + 1][col], row + 1, col))
    return heappop(pq)[0]

if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = kth_smallest(matrix, k)
    print(res)

