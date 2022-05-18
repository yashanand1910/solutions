from typing import List
from collections import deque

def get_valid_neighbors(node, grid):
    d_row = [0, -1, 0, 1]
    d_col = [-1, 0, 1, 0]
    for i in range(len(d_row)):
        new_row = node[0] + d_row[i]
        new_col = node[1] + d_col[i]
        if -1 < new_row < len(grid) and -1 < new_col < len(grid[0]):
            if grid[new_row][new_col] == 1:
                yield new_row, new_col

def count_number_of_islands(grid: List[List[int]]) -> int:
    # search the grid to find the next 1:
    number_of_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0: continue
            queue = deque([[i, j]])
            grid[i][j] = 0
            while len(queue) > 0:
               node = queue.popleft()
               for n in get_valid_neighbors(node, grid):
                   queue.append(n)
                   grid[n[0]][n[1]] = 0
            number_of_islands += 1
    return number_of_islands

if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)

