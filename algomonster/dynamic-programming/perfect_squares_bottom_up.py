from math import floor, sqrt

def perfect_squares(n: int) -> int:
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, floor(sqrt(i)) + 1):
            dp[i] = min(dp[i], 1 + dp[i - j**2])

    return dp[n]

if __name__ == '__main__':
    n = int(input())
    res = perfect_squares(n)
    print(res)

