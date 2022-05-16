class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(tree: Node) -> int:
    if tree is None:
        return 0
    
    return 1 + max(height(tree.left), height(tree.right))
        
def is_balanced(tree: Node) -> bool:
    if tree is None:
        return True

    return is_balanced(tree.left) and is_balanced(tree.right) and (2 > abs(height(tree.left) - height(tree.right)))
    

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
