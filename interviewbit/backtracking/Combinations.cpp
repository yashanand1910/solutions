vector<vector<int>> solve(int start, int A, int B) {
    if (B == 1) {
        vector<vector<int>> temp;
        for (int i = start; i <= A; i++) temp.push_back({i});
        return temp;
    }
    int i = start;
    vector<vector<int>> list;
    while (i <= A - B + 1) {
        vector<vector<int>> tempList = solve(start + 1, A, B - 1);
        for (int j = 0; j < tempList.size(); j++) {
            tempList[j].insert(tempList[j].begin(), i);
        }
        list.insert(list.end(), tempList.begin(), tempList.end());
        i++;
        start = i;
    }
    
    return list;
}

vector<vector<int> > Solution::combine(int A, int B) {
    vector<vector<int>> list;
    if (B > A) return list;
    
    list = solve(1, A, B);
    
    return list;
}
