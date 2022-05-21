from typing import List
from collections import deque

def construct_graph(n, prereqs):
    graph = { i: [] for i in range(n) }
    parents = { i: 0 for i in range(n) }
    for prereq in prereqs:
        graph[prereq[1]].append(prereq[0])
        parents[prereq[0]] += 1
    return graph, parents

def is_valid_course_schedule(n: int, prerequisites: List[List[int]]) -> bool:
    graph, parents = construct_graph(n, prerequisites)
    queue = deque()
    for i, count in parents.items():
        if count == 0:
            queue.append(i)
    res = []
    while queue:
        i = queue.popleft()
        res.append(i)
        for child in graph[i]:
            parents[child] -= 1
            if parents[child] == 0:
                queue.append(child)
    return len(res) == n

if __name__ == '__main__':
    n = int(input())
    prerequisites = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = is_valid_course_schedule(n, prerequisites)
    print('true' if res else 'false')

