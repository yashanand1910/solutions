def min_distance(word1: str, word2: str) -> int:
    n1, n2 = len(word1), len(word2)
    dp = [[float('inf')] * (n2 + 1) for _ in range(n1 + 1)]

    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n1][n2]

if __name__ == '__main__':
    word1 = input()
    word2 = input()
    res = min_distance(word1, word2)
    print(res)

