from typing import List
from collections import deque

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    def get_neighbors(i, j, visited):
        d_rows = [0, -1, 0, 1]
        d_cols = [-1, 0, 1, 0]
        for z in range(len(d_rows)):
            x = i + d_rows[z]
            y = j + d_cols[z]
            if 0 <= x < len(dungeon_map) and 0 <= y < len(dungeon_map[0]):
                if dungeon_map[x][y] > 0 and (x, y) not in visited:
                    yield x, y

    def bfs(i, j):
        queue = deque([[i, j]])
        level = 1
        visited = set()
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                for x, y in get_neighbors(node[0], node[1], visited):
                    queue.append([x, y])
                    visited.add((x, y))
                    dungeon_map[x][y] = min(level, dungeon_map[x][y])
            level += 1

    for i in range(len(dungeon_map)):
        for j in range(len(dungeon_map[0])):
            if dungeon_map[i][j] == 0:
                bfs(i, j)

    return dungeon_map

if __name__ == '__main__':
    dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(' '.join(map(str, row)))

