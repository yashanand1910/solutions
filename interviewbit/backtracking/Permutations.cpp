vector<vector<int>> solve(vector<int> &A) {
    if (A.size() == 1) {
        vector<vector<int>> temp({{A[0]}});    
        return temp;
    }
    
    vector<vector<int>> list;
    int i = 0; int tempVal;
    while(i < A.size()) {
        tempVal = A[0];
        A[0] = A[i];
        A[i] = tempVal;
        vector<int> temp;
        for (int j = 1; j < A.size(); j++) {
            temp.push_back(A[j]);
        }
        vector<vector<int>> tempList;
        
        tempList = solve(temp);
        for (int k = 0; k < tempList.size(); k++) {
            tempList[k].insert(tempList[k].begin(), A[0]);
        }
        i++;
        list.insert(list.end(), tempList.begin(), tempList.end());
    }
    return list;
}

vector<vector<int> > Solution::permute(vector<int> &A) {
    sort(A.begin(), A.end());
    
    vector<vector<int>> list;
    
    list = solve(A);
    
    return list;
}
