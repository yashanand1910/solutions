from typing import List

def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    n = len(weights)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(max_weight + 1):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(max_weight + 1):
            dp[i][j] = max(dp[i][j], (dp[i - 1][j - weights[i - 1]] + values[i - 1]) if j >= weights[i - 1] else 0, dp[i - 1][j]) 

    return dp[n][max_weight]

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    max_weight = int(input())
    res = knapsack(weights, values, max_weight)
    print(res)

