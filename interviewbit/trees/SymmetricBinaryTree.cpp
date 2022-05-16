/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
SameTree(TreeNode* A, TreeNode* B) {
    if (!A && !B) return 1;
    if (!A || !B) return 0;
    if (A->val != B->val) return 0;
    return isSameTree(A->left, B->left) & isSameTree(A->right, B->right);
}
 
TreeNode* invertTree(TreeNode* A) {
    if (!A) return NULL;
    
    TreeNode* temp = A->right;
    A->right = invertTree(A->left);
    A->left = invertTree(temp);
    
    return A;
}
 
int Solution::isSymmetric(TreeNode* A) {
    if (!A) return 1;
    
    return isSameTree(A->left, invertTree(A->right));
}
