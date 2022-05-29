def partition2(s: str) -> int:
    def is_palindrome(s) -> bool:
        if len(s) < 2: return True
        return s[0] == s[-1] and is_palindrome(s[1:-1])

    def dfs(s, start, memo):
        if start in memo: return memo[start]
        if len(s) - start < 2: return 1

        count = 0
        for i in range(1, len(s) - start + 1):
            if is_palindrome(s[start:start + i]):
                ans = dfs(s, start + i, memo)
                count += ans
                if start + i not in memo:
                    memo[start + i] = ans

        return count

    memo = {}
    return dfs(s, 0, memo)

if __name__ == '__main__':
    s = input()
    res = partition2(s)
    print(res)

