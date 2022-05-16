/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int maxDepth(TreeNode* A) {
    if (!A) return 0;
    return 1 + max(maxDepth(A->left), maxDepth(A->right));
} 
 
int Solution::isBalanced(TreeNode* A) {
    if (!A) return 1;
    
    if (abs(maxDepth(A->left) - maxDepth(A->right)) > 1) return 0;
    return isBalanced(A->left) && isBalanced(A->right);
}
