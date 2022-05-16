class Solution {
public:
    // Returns true if index a is smaller
    bool isSmaller(vector<vector<int>> &mat, int a, int b) {
        if (mat[b][0] == -1) {
            return true;
        }
        for (int i = 0; i < mat[0].size(); i++) {
            if (mat[a][i] == 1 && mat[b][i] == 0) {
                return false;
            } else if (mat[a][i] == 0 && mat[b][i] == 1) {
                return true;
            }
        }
        
        return a < b;
    }
    
    vector<int> kWeakestRows(vector<vector<int>> &mat, int k) {
        vector<int> result;
        
        for (int i = 0; i < k; i++) {
            int weakestIndex = 0;
            
            for (int j = 0; j < mat.size(); j++) {
                if (mat[j][0] == -1) {
                    continue;
                }
                if (isSmaller(mat, j, weakestIndex)) {
                    weakestIndex = j;
                }
            }
            
            mat[weakestIndex][0] = -1;
            result.push_back(weakestIndex);
        }
        
        return result;
    }
};