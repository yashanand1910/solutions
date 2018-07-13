vector<int> Solution::lszero(vector<int> &A) {
    unordered_map<int, int> sum;
    vector<int> output;
    
    sum.insert({-1, 0});
    
    for (int i = 0; i < A.size(); i++) {
        if (sum.find(i) == sum.end()) sum.insert({i, sum[i - 1]});
        else {
            
        }
    }
    
    return output;
}
