class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if i == j:
                    is_palindrome[i][j] = True
                else:
                    is_palindrome[i][j] = s[i] == s[j] and (True if j - i < 2 else is_palindrome[i+1][j-1])

        dp = [0] * n
        for i in range(1, n):
            min_cuts = float('inf')
            if is_palindrome[0][i]:
                continue
            for j in range(i, 0, -1):
                if is_palindrome[j][i]:
                    min_cuts = min(min_cuts, 1 + dp[j - 1])
            dp[i] = min_cuts

        return dp[n - 1]
