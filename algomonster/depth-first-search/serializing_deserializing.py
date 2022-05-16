class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return 'x'
    
    return str(root.val) + serialize(root.left) + serialize(root.right)

def deserialize(s):    
    def dfs(nodes):
        val = next(nodes)
        if val == 'x':
            return
        node = Node(int(val))
        node.left = dfs(nodes)
        node.right = dfs(nodes)
        return node
    
    return dfs(iter(s))
        

if __name__ == '__main__':
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def print_tree(root):
        if not root:
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)
    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))
