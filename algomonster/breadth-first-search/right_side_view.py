from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> List[int]:
    def bfs(root, list):
        queue = deque([root])
        right_most = root
        while len(queue) > 0:
            node = queue[0]
            left = node.left
            right = node.right
            right_most = (right if right else left) if not right_most else right_most
            if right_most is node:
                list.append(node.val)
                right_most = right if right else left
            queue.popleft()
            for child in [right, left]:
                if child: queue.append(child)
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
    res = binary_tree_right_side_view(root)
    print(' '.join(map(str, res)))

