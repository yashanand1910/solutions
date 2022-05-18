from typing import List
from collections import deque

def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    if a == b: return 0
    queue = deque([a])
    left_most = a
    path_length = -1 
    visited = set()
    while len(queue) > 0:
        node = queue.popleft()
        if node is left_most:
            path_length += 1
            left_most = None
        if node == b:
            break
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not left_most:
                    left_most = neighbor
                queue.append(neighbor)
                visited.add(neighbor)
    return path_length

if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)

