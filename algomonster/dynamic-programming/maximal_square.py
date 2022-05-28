from typing import List

def maximal_square(matrix: List[List[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    longest = 0

    for r in range(n):
        dp[r][0] = matrix[r][0]
        longest = max(dp[r][0], longest)

    for c in range(m):
        dp[0][c] = matrix[0][c]
        longest = max(dp[0][c], longest)

    for r in range(1, n):
        for c in range(1, m):
            if matrix[r][c] == 0:
                continue
            dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
            longest = max(longest, dp[r][c])

    return longest**2

if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = maximal_square(matrix)
    print(res)

