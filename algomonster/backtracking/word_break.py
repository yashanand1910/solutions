from typing import List

def word_break(s: str, words: List[str]) -> bool:
    memo = {}
    def dfs(path, memo):
        if len(path) >= len(s):
            if path == s:
                return True
            return False
        for i in words:
            if len(i)+len(path) > len(s):
                continue
            path += i
            if not path in memo:
                memo[path] = dfs(path, memo)
            if memo[path]:
                return True
            path = path[:-len(i)]
        return False
    return dfs("", memo)

if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')
