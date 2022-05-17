from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    def bfs(root):
        queue = deque([root])
        depth = 0
        leftest = root    
        while len(queue) > 0:
            node    = queue[0]
            left    = node.left
            right   = node.right
            if not left and not right:
                break
            leftest = (left if left else right) if not leftest else leftest 
            if node is leftest:
                leftest = left if left else right
                depth += 1
            queue.popleft()
            for child in [right, left]:
                if child: queue.append(child)
        return depth
    return bfs(root)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = binary_tree_min_depth(root)
    print(res)

