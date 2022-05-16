vector<vector<int>> addSubset(vector<vector<int>> list, int i, vector<int> &A) {
    if (i == A.size()) {
        return list;
    }
    if (i < 0) {
        vector<int> temp({});
        list.push_back(temp);
        return addSubset(list, i + 1, A);
    }
    int n = list.size();
    for (int j = 0; j < n; j++) {
        vector<int> temp(list[j]);
        temp.push_back(A[i]);
        list.push_back(temp);
    }
    return addSubset(list, i + 1, A);
}

bool compareVectors (vector<int> a, vector<int> b) {
    if (a.size() == 0) return true;
    if (b.size() == 0) return false;
    if (a[0] < b[0]) return true;
    else if (a[0] > b[0]) return false;
    else {
        int i = 0;
        while (a[i] == b[i] && i < a.size() - 1 && i < b.size() - 1) i++;
        if (a[i] < b[i]) return true;
        else if (a[i] > b[i]) return false;
        else return a.size() < b.size();
    }
}

vector<vector<int> > Solution::subsets(vector<int> &A) {
    sort(A.begin(), A.end());
    vector<vector<int>> list;
    
    list = addSubset(list, -1, A);
    sort(list.begin(), list.end(), compareVectors);
    
    return list;
}
