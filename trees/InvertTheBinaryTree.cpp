TreeNode* Solution::invertTree(TreeNode* A) {
    if (!A) return NULL;
    
    TreeNode* temp = A->right;
    A->right = invertTree(A->left);
    A->left = invertTree(temp);
    
    return A;
}
