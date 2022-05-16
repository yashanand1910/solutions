vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    vector<vector<int>> output;
    unordered_map<string, int> table;
    int count = 0;
    for (int i = 0; i < A.size(); i++) {
        string temp = A[i];
        sort(temp.begin(), temp.end());
        if (table.find(temp) != table.end()) {
            output[table[temp]].push_back(i + 1);
            count++;
        } else {
            output.push_back({i + 1});
            table.insert({temp, i - count});
        }
    }
    
    return output;
}
