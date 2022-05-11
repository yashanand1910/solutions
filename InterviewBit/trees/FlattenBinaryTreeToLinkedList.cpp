/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* traverseTillEnd(TreeNode* A) {
    while (A->right) A = A->right;
    return A;
}
 
TreeNode* Solution::flatten(TreeNode* A) {
    if (!A) return NULL;
    if (!A->left && !A->right) return A;
    
    TreeNode* right = A->right;
    A->right = flatten(A->left);
    A->left = NULL;
    
    (traverseTillEnd(A))->right = flatten(right);

    return A;
}
