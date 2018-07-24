vector<string> Solution::prefix(vector<string> &A) {
    vector<vector<pair<string, int>>> alpha(26);
    vector<string> output(A.size());
    
    for (int i = 0; i < A.size(); i++) alpha[A[i][0] - 'a'].push_back(make_pair(A[i], i));
    
    for (int i = 0; i < alpha.size(); i++) {
        if (alpha[i].size() > 0) {
            if (alpha[i].size() == 1) output[alpha[i][0].second] = alpha[i][0].first.substr(0, 1);
            else {
                vector<string> temp;
                for (auto p : alpha[i]) temp.push_back(p.first.substr(1, p.first.size() - 1));
                char a = alpha[i][0].first[0];
                temp = prefix(temp);
                for (int j = 0; j < temp.size(); j++) output[alpha[i][j].second] = a + temp[j];
            }
        }
    }
    
    return output;
}
