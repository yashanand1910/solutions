class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def dfs(root: Node, min: int, max: int) -> bool:
        if not root:
            return True
        if root.val < min or root.val > max:
            return False
        return dfs(root.left, min, root.val) and dfs(root.right, root.val, max)
        
    return dfs(root, -1, 9999999)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')
