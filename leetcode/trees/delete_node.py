# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
            if not root:
                return

            if key < root.val:
                root.left = dfs(root.left, key)
                return root
            elif key > root.val:
                root.right = dfs(root.right, key)
                return root
            else:
                # key == root.val
                left = root.left
                right = root.right
                # TODO try del root

                if left and right:
                    # find min node in right subtree and replace with root
                    cur = right
                    while cur.left:
                        cur = cur.left
                    root.val = cur.val
                    root.right = dfs(root.right, cur.val)
                    return root

                if left:
                    return left
                return right
            
        return dfs(root, key)
        