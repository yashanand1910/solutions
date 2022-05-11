/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* Solution::sortedArrayToBST(const vector<int> &A) {
    if (A.size() == 0) return NULL;
    if (A.size() == 1) return new TreeNode(A[0]);
 
    int mid = (A.size() - 1) / 2;
    TreeNode* root = new TreeNode(A[mid]);
    vector<int> left, right;
    
    for (int i = 0; i < mid; i++) left.push_back(A[i]);
    for (int i = mid + 1; i < A.size(); i++) right.push_back(A[i]);
    
    root->left = sortedArrayToBST(left);
    root->right = sortedArrayToBST(right);
    
    return root;
}
