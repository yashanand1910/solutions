from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.freq = 0

    def insert(self, s, i = 0):
        self.freq += 1
        if i < len(s):
            self.children.setdefault(s[i], Node(s[i]))
            self.children.get(s[i]).insert(s, i + 1)

def autocomplete(words: List[str]) -> int:
    trie = Node('$')

    res = 0
    for word in words:
        trie.insert(word)
        cur = trie
        count = 100001
        strokes = 0
        for i, letter in enumerate(word):
            cur = cur.children[letter]
            if cur.freq <= 1:
                strokes = i + 1
                break
        res += strokes if strokes else len(word)

    return res

if __name__ == '__main__':
    words = input().split()
    res = autocomplete(words)
    print(res)

