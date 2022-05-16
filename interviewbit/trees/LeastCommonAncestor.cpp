/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int searchBoth(TreeNode* A, int B, int C) {
    if (!A) return 0;
    int found = 0;
    if (A->val == B) found++;
    if (A->val == C) found++;
    if (found == 2) return found;
    found += searchBoth(A->left, B, C) + searchBoth(A->right, B, C);
    return found;
} 
 
int Solution::lca(TreeNode* A, int B, int C) {
    if (searchBoth(A, B, C) < 2) return -1;
    
    int left = searchBoth(A->left, B, C), right = searchBoth(A->right, B, C);
    if (left < 2 && right < 2) return A->val;
    return lca(left > right ? A->left : A->right, B, C);
}
