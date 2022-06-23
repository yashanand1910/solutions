from typing import List

class Trie:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.word = -1

    def insert(self, s, index, i=0):
        if i == len(s):
            self.word = index
            return
        self.next.setdefault(s[i], Trie(s[i]))
        self.next[s[i]].insert(s, index, i+1)

def get_directions(matrix, i, j):
    if i == -1:
        yield 0, 0
        return
    h = len(matrix)
    w = len(matrix[0])
    moves = [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
    for x, y in moves:
        if 0 <= x < h and  0 <= y < w:
            yield x, y

def word_search_ii(matrix: List[str], words: List[str]) -> List[str]:
    trie = Trie('$')
    found = []
    for i, word in enumerate(words):
        found.append(False)
        trie.insert(word, i)

    def dfs(matrix, i, j, word, visited, cur):
        if cur.word >= 0:
            found[cur.word] = True
            cur.word = -1
        for x, y in get_directions(matrix, i, j):
            if not visited[x][y] and matrix[x][y] in cur.next:
                visited[x][y] = True
                dfs(matrix, x, y, word + matrix[x][y], visited, cur.next[matrix[x][y]])
                visited[x][y] = False

    h = len(matrix)
    w = len(matrix[0])
    visited = [[False] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if matrix[i][j] in trie.next:
                visited[i][j] = True
                dfs(matrix, i, j, matrix[i][j], visited, trie.next[matrix[i][j]])
                visited[i][j] = False
    
    res = []
    for i in range(len(found)):
        if found[i]:
            res.append(words[i])
    return res

if __name__ == '__main__':
    matrix = input().split()
    words = input().split()
    res = word_search_ii(matrix, words)
    print(' '.join(res))

