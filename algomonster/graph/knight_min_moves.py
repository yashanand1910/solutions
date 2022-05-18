from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    if x == 0 and y == 0: return 0

    def get_neighbors(node, visited, min_row, max_row, min_col, max_col):
        d_row = [-1, -2, -2, -1, 1, 2, 2, 1]
        d_col = [-2, -1, 1, 2, 2, 1, -1, -2]
        for i in range(len(d_row)):
            new_row = node[0] + d_row[i]
            new_col = node[1] + d_col[i]
            if min_row <= new_row <= max_row and min_col <= new_col <= max_col:
                if visited[new_row - min_row][new_col - min_col] == 0:
                    yield new_row, new_col
    
    def bfs():
        min_row = min(-1, x - 2) 
        max_row = max(1, x + 2)
        min_col = min(0, y - 2)
        max_col = max(0, y + 2)
        visited = []
        for i in range(max_col - min_col + 1):
            visited.append([0] * (max_col - min_col + 1))
        queue = deque([[0, 0]])
        visited[0 - min_row][0 - min_col] = 1
        depth = 1
        while len(queue) > 0:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                for n in get_neighbors(node, visited, min_row, max_row, min_col, max_col):
                    if n[0] == x and n[1] == y:
                        return depth
                    queue.append(n)
                    visited[n[0] - min_row][n[1] - min_col] = 1
            depth += 1     
        return depth # not found

    return bfs()
                
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)

