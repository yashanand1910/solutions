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

def prefix_count(words: List[str], prefixes: List[str]) -> List[int]:
    res = []
    trie = Node('$')
    for word in words:
        trie.insert(word)

    for prefix in prefixes:
        cur = trie
        count = 0
        for i, letter in enumerate(prefix):
            if letter in cur.children:
                cur = cur.children[letter]
                count = cur.freq
            else:
                count = 0
                break
        res.append(count)

    return res

if __name__ == '__main__':
    words = input().split()
    prefixes = input().split()
    res = prefix_count(words, prefixes)
    print(' '.join(map(str, res)))

