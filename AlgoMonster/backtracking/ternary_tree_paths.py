from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    list = []
    def dfs(path, node):
        if all(child is None for child in node.children):
            path.append(str(node.val))
            list.append('->'.join(path))
            return
        path.append(str(node.val))
        for child in node.children:
            dfs(path, child)
            path.pop()
    dfs([], root)
    return list

def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
