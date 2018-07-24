/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int Solution::minDepth(TreeNode* A) {
    if (!A) return 0;
    
    int minD = INT_MAX;
    if (A->left) minD = min(minD, 1 + minDepth(A->left));
    if (A->right) minD = min(minD, 1 + minDepth(A->right));
    
    return minD;
}
