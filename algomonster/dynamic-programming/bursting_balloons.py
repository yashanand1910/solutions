from typing import List

def festival_game(target: List[int]) -> int:
    n = len(target)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = (target[i - 1] if i > 0 else 1) * target[i] * (target[i + 1] if i < (n-1) else 1)

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], (dp[i][k-1] if k > i else 0) + (dp[k + 1][j] if k < j else 0) + ((target[i-1] if i > 0 else 1) * target[k] * (target[j+1] if j < (n-1) else 1)))

    return dp[0][n-1]

if __name__ == '__main__':
    target = [int(x) for x in input().split()]
    res = festival_game(target)
    print(res)

