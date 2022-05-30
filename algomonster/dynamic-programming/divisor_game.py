def divisor_game(n: int) -> bool:
    dp = [False] * (n + 1)

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = dp[i] or not dp[i - j]

    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    res = divisor_game(n)
    print('true' if res else 'false')

