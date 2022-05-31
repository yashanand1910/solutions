class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        maximum = (0, 0, 0)

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if j - i > 1:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = True
                if dp[i][j]:
                    maximum = max(maximum, (j - i, i, j))

        return s[maximum[1]:maximum[2] + 1]

