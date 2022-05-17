from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
    def bfs(root, list):
        queue = deque([root])
        direction = True
        left_most = root
        while len(queue) > 0:
            node = queue[0]
            left = node.left if node else None
            right = node.right if node else None
            left_most = (left if left else right) if left_most is None else left_most
            if node is left_most:
                list.append([])
                for i in range(len(queue)):
                    list[-1].append(queue[i if direction else (-1 - i)].val)
                direction = not direction
                left_most = left if left else right
            queue.popleft()
            for child in [left, right]:
                if child:
                    queue.append(child)
        return list
    return bfs(root, [])

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))


