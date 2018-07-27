/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
priority_queue<int, vector<int>, greater<int>> que;

void traverseAllNodes(TreeNode* A) {
    if (!A) return;
    que.push(A->val);
    traverseAllNodes(A->left);
    traverseAllNodes(A->right);
}
 
int Solution::kthsmallest(TreeNode* A, int B) {
    while (!que.empty()) que.pop();
    traverseAllNodes(A);
    
    while(--B) que.pop();
    return que.top();
}
