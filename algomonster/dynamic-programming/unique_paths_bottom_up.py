def unique_paths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for r in range(m):
        dp[r][0] = 1
    for c in range(n):
        dp[0][c] = 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[-1][-1]

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    res = unique_paths(m, n)
    print(res)

