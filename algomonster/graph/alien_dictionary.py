from typing import List
from collections import deque

def construct_graph(words, letters):
    graph = { letter: [] for letter in letters }
    parents = { letter: 0 for letter in letters } 
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        n = 0
        while a[n] == b[n] and n < len(a) - 1 and n < len(b) - 1:
            n += 1
        graph[a[n]].append(b[n])
        parents[b[n]] += 1
    return graph, parents

def alien_order(words: List[str]) -> str:
    letters = set()
    for word in words:
        for letter in list(word):
            letters.add(letter)
    graph, parents  = construct_graph(words, letters)
    queue = deque()
    for letter, count in parents.items():
        if count == 0:
            queue.append(letter)
    res = '' 
    while queue:
        sorted_list = list(queue)
        sorted_list.sort()
        queue = deque(sorted_list)
        node = queue.popleft()
        res += node
        for child in graph[node]:
            parents[child] -= 1
            if parents[child] == 0:
                queue.append(child)
    if len(res) == len(letters):
        return res
    return ''

if __name__ == '__main__':
    words = input().split()
    res = alien_order(words)
    print(res)

