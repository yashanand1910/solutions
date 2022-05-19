from collections import deque
from typing import List

def num_steps(combo: str, trapped_combos: List[str]) -> int:
    start = '0000'

    def get_next_possible_combos(node, visited):
        options = [0, 1, -1]
        for i in range(len(node)):
            for j in options:
                code = list(map(int, node))
                code[i] = (10 + code[i] + options[j]) % 10
                next = "".join(list(map(str, code)))
                if next not in trapped_combos and next not in visited:
                    yield next

    def bfs():
        queue = deque([start])
        steps = 1
        visited = set()
        visited.add(start)
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                for next in get_next_possible_combos(node, visited):
                    if next == combo:
                        return steps
                    queue.append(next)
                    visited.add(next)
            steps += 1
        return -1
    
    return bfs()

if __name__ == '__main__':
    combo = input()
    trapped_combos = input().split()
    res = num_steps(combo, trapped_combos)
    print(res)


