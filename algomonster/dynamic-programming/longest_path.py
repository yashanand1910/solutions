from typing import List

def longest_path(graph: List[List[int]]) -> int:
    n = len(graph)
    dp = [0 for _ in range(100001)]
    has_parent = [False for _ in range(100001)]

    for i in range(n):
        for j in graph[i]:
            has_parent[j] = True
    
    def dfs(cur):
        if cur < n:
            if dp[cur]: return dp[cur]
        else:
            return 0

        maximum = 0
        for i in graph[cur]:
            ans = dfs(i)
            if not dp[i]: dp[i] = ans
            maximum = max(maximum, 1 + ans)

        return maximum

    maximum = 0
    for i in range(n):
        if not has_parent[i]:
            maximum = max(maximum, dfs(i))

    return maximum

if __name__ == '__main__':
    adj = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = longest_path(adj)
    print(res)

