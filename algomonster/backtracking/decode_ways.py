def decode_ways(digits: str) -> int:
    def dfs(s, memo):
        if len(s)<=1:
            memo[s] = 1
            return 1
        count = 0
        for i in range(1, min(len(s)+1, 3)):
            if int(s[:i])<=26:
                if s[i:] not in memo:
                    memo[s[i:]] = dfs(s[i:], memo)
                count += memo[s[i:]]
        return count
    memo = {}
    return dfs(digits, memo)

if __name__ == '__main__':
    digits = input()
    res = decode_ways(digits)
    print(res)
