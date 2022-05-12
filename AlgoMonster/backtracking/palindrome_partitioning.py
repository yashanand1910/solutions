from typing import List

def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    return s[0]==s[-1] and is_palindrome(s[1:-1]) 

def partition(s: str) -> List[List[str]]:
    def dfs(path, cur, list):
        if len(cur) <= 1:
            if len(cur) == 1:
                path.append(cur)
            list.append(path[:])
            if len(cur) == 1:
                path.pop()
            return
        for i in range(1, len(cur) + 1):
            substr = cur[:i]
            if is_palindrome(substr):
                path.append(substr)
                dfs(path, cur[i:], list)
                path.pop()
    list = []
    dfs([], s, list)
    return list

if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))
