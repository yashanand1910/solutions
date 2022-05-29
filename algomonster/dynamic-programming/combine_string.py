def combine_string(s1: str, s2: str, s3: str) -> bool:
    n1 = len(s1)
    n2 = len(s2)
    n3 = len(s3)

    if n1 + n2 != n3: return False

    dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

    dp[0][0] = True

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if not (i or j): continue
            flag = False
            if j > 0 and dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]:
                flag = True
                dp[i][j] = True
            if i > 0 and dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]:
                flag = True
                dp[i][j] = True
            if not flag: 
                dp[i][j] = False

    return dp[n1][n2]

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s3 = input()
    res = combine_string(s1, s2, s3)
    print('true' if res else 'false')

