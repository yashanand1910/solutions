from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    dp = [[float('inf') for _ in range(m)] for _ in range(n)]
    dp[0][0] = grid[0][0]
    for r in range(1, n):
        dp[r][0] = dp[r - 1][0] + grid[r][0]
    for c in range(1, m):
        dp[0][c] = dp[0][c - 1] + grid[0][c]

    for r in range(1, n):
        for c in range(1, m):
            dp[r][c] = min(dp[r][c], dp[r - 1][c] + grid[r][c], dp[r][c - 1] + grid[r][c])

    return dp[-1][-1]

if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_path_sum(grid)
    print(res)

