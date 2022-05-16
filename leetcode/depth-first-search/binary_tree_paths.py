# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        list = []
        
        # using same list so no extra memory is used
        def dfs(root) -> int:
            n = 0
            if not root:
                return

            if not root.left and not root.right:
                list.append(str(root.val))
                n += 1

            if root.left:
                for i in range(dfs(root.left)):
                    list[-1-i] = f'{root.val}->{list[-1-i]}'
                    n += 1
            if root.right:
                for i in range(dfs(root.right)):
                    list[-1-i] = f'{root.val}->{list[-1-i]}'
                    n += 1
            return n
        
        dfs(root)
        return list
            