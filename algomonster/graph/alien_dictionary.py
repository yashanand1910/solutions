from typing import List
from collections import deque

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def construct_graph(words, letters):
    graph = { letter: [] for letter in letters }
    for word in words:
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                graph[word[i]].append(word[i + 1])
    return graph

def count_parents(graph):
    count = [0] * 26
    for parent in graph:
        for child in graph[parent]:
            count[ord(child) - 97] += 1
    return count

def alien_order(words: List[str]) -> str:
    letters = set()
    for word in words:
        for letter in list(word):
            letters.add(letter)
    graph = construct_graph(words, letters)
    parents = count_parents(graph)
    queue = deque()
    for i, count in enumerate(parents):
        if chr(i + 97) in letters and count == 0:
            queue.append(chr(i + 97))
    res = '' 
    while queue:
        node = queue.popleft()
        res += node
        for child in graph[node]:
            parents[ord(child) - 97] -= 1
            if parents[ord(child) - 97] == 0:
                queue.append(child)
    return res

if __name__ == '__main__':
    words = input().split()
    res = alien_order(words)
    print(res)

