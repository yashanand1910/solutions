from typing import List

def plumber(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    # work on first row
    i = 0
    while i < m:
        coins = 0
        last_start = i
        while i < m and grid[0][i] != -1:
            coins += grid[0][i]
            i += 1
        for j in range(last_start, i):
            dp[0][j] = coins
        i += 1

    for r in range(1, n):
        max_row = -1
        i = 0
        while i < m:
            last_start = i
            coins = 0
            max_upper = -1
            while i < m and grid[r][i] != -1:
                coins += grid[r][i]
                max_upper = max(max_upper, dp[r - 1][i])
                i += 1
            if max_upper != -1:
                max_row = max(max_row, coins + max_upper)
                for j in range(last_start, i):
                    dp[r][j] = coins + max_upper
            while i < m and grid[r][i] == -1:
                i += 1
        if r == n - 1:
            return max_row

if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = plumber(grid)
    print(res)

