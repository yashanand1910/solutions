vector<vector<int> > solve(vector<int> &A, int B) {
    vector<vector<int>> output;
    
    for (int i = 0; i < A.size(); i++) {
        if (B - A[i] > 0) {
            vector<int> newA;
            for (int j = i + 1; j < A.size(); j++)  newA.push_back(A[j]);
            vector<vector<int>> temp = solve(newA, B - A[i]);
            if (temp.size() > 0) {
                for (int j = 0; j < temp.size(); j++) temp[j].insert(temp[j].begin(), A[i]);
                output.insert(output.end(), temp.begin(), temp.end());
            }
        } else if (B - A[i] == 0) output.push_back({A[i]});
    }
    
    return output;
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

vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    sort(A.begin(), A.end());
    vector<vector<int>> output = solve(A, B);
    sort(output.begin(), output.end(), compareVectors);
    output.erase( unique( output.begin(), output.end() ), output.end() );
    return output;
}