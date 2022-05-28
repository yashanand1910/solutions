from typing import List

def max_layers(envelopes: List[List[int]]) -> int:
    if not envelopes: return 0
    envelopes.sort(key=lambda x: x[0] + x[1])
    n = len(envelopes)
    dp = [1 for _ in range(n)]
    res = 1
    for i in range(1, n):
        for j in range(i):
            if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])

    return res

if __name__ == '__main__':
    envelopes = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = max_layers(envelopes)
    print(res)

