from typing import List

def delete_string(costs: List[int], s1: str, s2: str) -> int:
    n1, n2 = len(s1), len(s2)
    dp = [[float('inf')] * (n2 + 1) for _ in range(n1 + 1)]

    dp[0][0] = 0
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + costs[ord(s1[i - 1]) - 97]
    for j in range(1, n2 + 1):
        dp[0][j] += dp[0][j - 1] + costs[ord(s2[j - 1]) - 97]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(costs[ord(s1[i - 1]) - 97] + dp[i - 1][j], costs[ord(s2[j - 1]) - 97] + dp[i][j - 1])

    return dp[n1][n2]

if __name__ == '__main__':
    costs = [int(x) for x in input().split()]
    s1 = input()
    s2 = input()
    res = delete_string(costs, s1, s2)
    print(res)

