/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<vector<int> > Solution::zigzagLevelOrder(TreeNode* A) {
    int dir = 0;
    stack<TreeNode*> st;
    vector<vector<int> > output;
    
    if (!A) return output;
    
    st.push(A);
    output.push_back({A->val});
    
    while (!st.empty()) {
        stack<TreeNode*> stKids;
        vector<int> kidsVal;
        while (!st.empty()) {
            if (dir == 0) {
                if (st.top()->right) {
                    stKids.push(st.top()->right);
                    kidsVal.push_back((st.top()->right)->val);
                }
                if (st.top()->left) {
                    stKids.push(st.top()->left);
                    kidsVal.push_back((st.top()->left)->val);
                }
            } else {
                if (st.top()->left) {
                    stKids.push(st.top()->left);
                    kidsVal.push_back((st.top()->left)->val);
                }
                if (st.top()->right) {
                    stKids.push(st.top()->right);
                    kidsVal.push_back((st.top()->right)->val);
                }
            }
            st.pop();
        }
        dir = dir == 0? 1 : 0;
        st = stKids;
        if (kidsVal.size()) output.push_back(kidsVal);
        kidsVal.clear();
    }
    
    return output;
}
