/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int isValidBSTUtil(TreeNode* A, int mini, int maxi) {
    if (A == NULL) return 1;
    if (A->val >= maxi || A->val <= mini) return 0;
    else return isValidBSTUtil(A->left, mini, A->val) && isValidBSTUtil(A->right, A->val, maxi);
}

int Solution::isValidBST(TreeNode* A) {
    return isValidBSTUtil(A, INT_MIN, INT_MAX);
}
