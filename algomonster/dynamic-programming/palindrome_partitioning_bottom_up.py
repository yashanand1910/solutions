def partition2(s: str) -> int:
    n = len(s)
    is_palindrome = [[False] * n for _ in range(n)]

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if i == j:
                is_palindrome[i][j] = True
            else:
                is_palindrome[i][j] = s[i] == s[j] and (is_palindrome[i+1][j-1] if (j-i) > 1 else True)

    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        for j in range(i, 0, -1):
            if is_palindrome[j][i]:
                dp[i] += dp[j - 1]
        if is_palindrome[0][i]:
            dp[i] += 1

    return dp[n - 1]

if __name__ == '__main__':
    s = input()
    res = partition2(s)
    print(res)

