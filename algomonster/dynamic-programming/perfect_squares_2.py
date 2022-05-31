from math import floor, sqrt
from functools import lru_cache

def perfect_squares_2(n: int) -> int:
    used = [False] * (floor(sqrt(n)) + 1)

    @lru_cache(None)
    def dfs(n):
        if n < 0:
            return float('inf')
        if n == 0:
            return 0

        minimum = float('inf')
        for i in range(1, floor(sqrt(n)) + 1):
            if not used[i]:
                used[i] = True
                minimum = min(minimum, 1 + dfs(n - i**2))
                used[i] = False
        
        return minimum

    ans = dfs(n)
    return -1 if ans == float('inf') else ans

if __name__ == '__main__':
    n = int(input())
    res = perfect_squares_2(n)
    print(res)

