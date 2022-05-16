from typing import List

def permutations(letters: str) -> List[str]:
    list = []
    def dfs(path, used):
        if len(path) == len(letters):
            list.append(''.join(path))
            return
        for i, letter in enumerate(letters):
            if used[i]:
                continue
            used[i] = True
            path.append(letter)
            dfs(path, used)
            path.pop()
            used[i] = False
    dfs([], [False]*len(letters))
    return list

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in res:
        print(line)
        