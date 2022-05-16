from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    def bfs(root, res):
        queue = deque([root])
        left_most = root
        while len(queue) > 0:
            if queue[0] is left_most:
                res.append(map(lambda x: x.val, list(queue)))
                left_most = queue[0].left if queue[0].left else queue[0].right
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
    res = []
    return bfs(root, res)
            
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))

