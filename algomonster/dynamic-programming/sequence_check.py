def sequence_check(s: str, t: str) -> int:
    n1 = len(s)
    n2 = len(t)
    if n1 < n2: return 0

    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if j == 0: 
                dp[i][j] = 1 
                continue
            if i < j: continue

            dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - 1] if (s[i - 1] == t[j - 1]) else 0)

    return dp[n1][n2]

if __name__ == '__main__':
    s = input()
    t = input()
    res = sequence_check(s, t)
    print(res)

