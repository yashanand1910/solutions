from typing import List

def train_ride(n: int, k: int, connections: List[List[int]]) -> int:
    dp = [[-1] * n for i in range(n)]
    
    def get_line(i, j):
        return dp[i-1][j-1]

    def set_line(i, j, val):
        if dp[i-1][j-1] != -1:  
            val = min(val, dp[i-1][j-1])
            dp[i-1][j-1] = val
            dp[j-1][i-1] = val
        else:
            dp[i-1][j-1] = val
            dp[j-1][i-1] = val

    for i, j, line in connections:
        set_line(i, j, line)

    def dfs(cur, visited, price):
        if cur == n:
            return price
        min_price = float('inf')
        for i in range(1, n+1):
            if not visited[i-1] and get_line(cur, i) != -1:
                visited[i-1] = True
                ans = dfs(i, visited, max(price, get_line(cur, i)))
                visited[i-1] = False
                if ans != -1:
                    min_price = min(min_price, ans)
        return min_price

    visited = [False for i in range(n)]
    visited[0] = True
    ans = dfs(1, visited, 0)
    return ans if ans != float('inf') else -1

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    connections = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = train_ride(n, k, connections)
    print(res)

