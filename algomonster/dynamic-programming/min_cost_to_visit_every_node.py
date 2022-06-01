from typing import List

def min_cost_to_visit_every_node(graph: List[List[int]]) -> int:
    n = len(graph)
    dp = [[0] * n for _ in range((1 << n))]

    def f(cur, used):
        if dp[used][cur]: return dp[used][cur]
        if used == (1 << n) - 1: return 0

        minimum = float('inf')
        for i in range(len(graph[cur])):
            if (used & (1 << i)) or not graph[cur][i]:
                continue
            new_used = (used | (1 << i))
            ans = f(i, new_used)
            if not dp[new_used][i]: dp[new_used][i] = ans
            minimum = min(minimum, graph[cur][i] + ans)

        return minimum

    ans = f(0, 1)
    return ans if ans != float('inf') else -1

if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_cost_to_visit_every_node(graph)
    print(res)

