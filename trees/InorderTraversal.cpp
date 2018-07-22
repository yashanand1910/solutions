/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

vector<int> Solution::inorderTraversal(TreeNode* root) {
    vector<int> output; stack<TreeNode*> st;
    if (!root) return output;
    
    while (root != NULL) {
        while (root->left) {
            st.push(root);
            root = root->left;
        }
        output.push_back(root->val);
        
        if (root->right) root = root->right;
        else {
            while (!st.empty() && !st.top()->right) {
                output.push_back(st.top()->val);
                st.pop();
            }
            if (!st.empty()) {
                output.push_back(st.top()->val);
                root = st.top()->right;
                st.pop();
            } else root = NULL;
        }
    }        
    
    return output;
}
