from typing import List

def longest_cycle(n: int, edges: List[List[int]]) -> int:
    children = [[] for _ in range(n + 1)]
    for a, b in edges:
        children[a].append(b)
        children[b].append(a)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    def dfs(cur, prev):
        if dp[cur][prev]: return dp[cur][prev]
        if cur != prev and len(children[cur]) == 1: return 0

        maximum = 0
        for child in children[cur]:
            if child == prev: continue
            ans = dfs(child, cur)
            if not dp[child][cur]: dp[child][cur] = ans
            maximum = max(maximum, 1 + ans)

        return maximum

    longest_path = 0
    for i in range(len(children)):
        if len(children[i]) == 1:
            longest_path = max(longest_path, dfs(i, i))

    return longest_path + 1

if __name__ == '__main__':
    n = int(input())
    edges = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = longest_cycle(n, edges)
    print(res)

