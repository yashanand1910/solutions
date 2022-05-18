from typing import List
from collections import deque

def get_neighbors(node: List[int], image: List[List[int]]):
    neighbors = []
    delta_col = [-1, 0, 1, 0]
    delta_row = [0, -1, 0, 1]
    for i in range(4):
        new_row = node[0] + delta_row[i] 
        new_col = node[1] + delta_col[i]
        if new_row < 0 or new_row >= len(image): continue
        if new_col < 0 or new_col >= len(image[0]): continue
        neighbors.append([new_row, new_col])
    return neighbors

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    queue = deque([[r, c]])
    original = image[r][c]
    image[r][c] = replacement
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node, image):
            if image[neighbor[0]][neighbor[1]] == original:
                queue.append(neighbor)
                image[neighbor[0]][neighbor[1]] = replacement
    return image

if __name__ == '__main__':
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(' '.join(map(str, row)))

