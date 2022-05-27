def unique_paths(m: int, n: int) -> int:
    def dfs(m, n, memo):
        if (m, n) in memo: return memo[(m, n)]
        if m == 1 or n == 1:
            return 1
        path_1 = dfs(m - 1, n, memo)
        if (m - 1, n) not in memo: memo[(m - 1, n)] = path_1
        path_2 = dfs(m, n - 1, memo)
        if (m, n - 1) not in memo: memo[(m, n - 1)] = path_2
        return path_1 + path_2
    memo = {}
    return dfs(m, n, memo)

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    res = unique_paths(m, n)
    print(res)

