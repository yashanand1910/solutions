/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* findNode(TreeNode* root, int val) {
    if (!root) return NULL;
    while (root->val != val) {
        if (val <= root->val) root = root->left;
        else root = root->right;
    }
    return root;
}

TreeNode* findMinNode(TreeNode* root) {
    if (!root) return NULL;
    while (root->left) root = root->left;
    return root;
}

TreeNode* Solution::getSuccessor(TreeNode* A, int B) {
    TreeNode* current = findNode(A, B);
    
    if (current->right) return findMin(current->right);
    else {
        TreeNode* successor = NULL;
        TreeNode* ancestor = A;
        while (ancestor != current) {
            if (B < ancestor->val) {
                successor = ancestor;
                ancestor = ancestor -> left;
            } else ancestor = ancestor->right;
        }
        
        return successor;
    }
}
