from typing import List

def minimum_total(triangle: List[List[int]]) -> int:
    if not triangle: return 0
    h = len(triangle)
    b = len(triangle[-1])
    dp = []
    for i in range(h):
        arr = [float('inf')] * len(triangle[i])
        dp.append(arr)
    for i in range(b):
        dp[-1][i] = triangle[-1][i]
    for i in range(1, h):
        for j in range(len(triangle[-1-i])):
            dp[-1-i][j] = triangle[-1-i][j] + min(dp[-i][j], dp[-i][j+1])
    return dp[0][0]

if __name__ == '__main__':
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)

