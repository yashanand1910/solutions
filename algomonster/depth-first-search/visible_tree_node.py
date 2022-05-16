class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_count(node: Node, max_above: int) -> int:
    if node == None:
        return 0
    
    if node.val >= max_above or max_above == -1:
        return 1 + visible_count(node.left, node.val) + visible_count(node.right, node.val)
    
    return visible_count(node.left, max_above) + visible_count(node.right, max_above)
        
def visible_tree_node(root: Node) -> int:
    return visible_count(root, -1)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)
