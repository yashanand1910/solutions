def palindrome_counting(s: str) -> int:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    res = 0

    for l in range(1, n  + 1):
        for i in range(0, n - l + 1):
            if l == 1:
                dp[i][i + l - 1] = True
                res += 1
            else:
                if s[i] == s[i + l - 1]:
                    if l == 2:
                        dp[i][i + l - 1] = True
                        res += 1
                    elif dp[i + 1][i + l - 2]:
                        dp[i][i + l - 1] = True
                        res += 1
    return res

if __name__ == '__main__':
    s = input()
    res = palindrome_counting(s)
    print(res)

