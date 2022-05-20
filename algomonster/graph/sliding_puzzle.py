from typing import List
from collections import deque

directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
target = ((1, 2, 3), (4, 5, 0))

def num_steps(init_pos: List[List[int]]) -> int:
    init_tuple = tuple(tuple(line) for line in init_pos)
    if init_tuple == target:
        return 0
    queue = deque([init_tuple])
    pos_map = {
        init_tuple: 0
    }
    while queue:
        node = queue.popleft()
        x, y = 0, 0
        for i in range(2):
            for j in range(3):
                if node[i][j] == 0:
                    x, y = i, j
        for dir in directions:
            i, j = x + dir[0], y + dir[1]
            if 0 <= i < 2 and 0 <= j < 3:
                node_list = list(list(line) for line in node)
                node_list[x][y], node_list[i][j] = node_list[i][j], node_list[x][y]
                node_tuple = tuple(tuple(line) for line in node_list)
                if node_tuple not in pos_map:
                    pos_map[node_tuple] = pos_map[node] + 1
                    queue.append(node_tuple)
                    if target == node_tuple:
                        return pos_map[node_tuple]
    return -1

if __name__ == '__main__':
    init_pos = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = num_steps(init_pos)
    print(res)

