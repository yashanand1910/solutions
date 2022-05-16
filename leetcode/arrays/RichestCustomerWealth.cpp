class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        
        for (int i = 0; i < accounts.size(); i++) {
            int wealth = 0;
            
            for (int j = 0; j < accounts[0].size(); j++) {
                wealth += accounts[i][j];
            }
            
            if (wealth > maxWealth) {
                maxWealth = wealth;
            }
        }
        
        return maxWealth;
    }
};