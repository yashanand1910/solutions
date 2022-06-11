from collections import deque
from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closest_values(bst: Node, x: int, k: int) -> List[int]:
    stack = []
    range = deque()

    def fill(node: Node):
        cur = node
        while cur:
            stack.append(cur)
            cur = cur.left

    fill(bst)

    min_distance = float('inf')
    closest_range = []

    while stack:
        node = stack.pop()
        range.append(node)
        if len(range) > k:
            range.popleft()
        if len(range) == k:
            new_distance = max(abs(x-range[0].val), abs(x-range[-1].val))
            if new_distance < min_distance:
                min_distance = new_distance
                closest_range = [i.val for i in range]
        if node.right:
            fill(node.right)

    return closest_range

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    x = int(input())
    k = int(input())
    res = closest_values(bst, x, k)
    print(' '.join(map(str, res)))

