from typing import List
from collections import deque

def construct_graph(original, seqs):
    graph = { node: [] for node in original }
    for seq in seqs:
        for i in range(len(seq) - 1):
            graph[seq[i]].append(seq[i + 1])
    return graph

def count_parents(graph):
    count = { node: 0 for node in graph.keys() }
    for parent in graph:
        for child in graph[parent]:
            count[child] += 1
    return count

def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    graph = construct_graph(original, seqs)
    parents = count_parents(graph)
    queue = deque()
    for node, count in parents.items():
        if count == 0:
            queue.append(node)
    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        flag = False
        for child in graph[node]:
            parents[child] -= 1
            if parents[child] == 0:
                if flag:
                    return False
                flag = True
                queue.append(child)
    return  tuple(original) == tuple(res)

if __name__ == '__main__':
    original = [int(x) for x in input().split()]
    seqs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = sequence_reconstruction(original, seqs)
    print('true' if res else 'false')

