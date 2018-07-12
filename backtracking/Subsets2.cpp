vector<vector<int>> solve(vector<int> &A, vector<vector<int>> cur, int pos, int lastEnd) {
    if (pos == A.size()) return cur;
    if (pos < 0) {
        vector<int> temp({});
        cur.push_back(temp);
        return solve(A, cur, pos + 1, 1);
    }
    int n = cur.size(), i;
    if (A[pos] == A[pos - 1]) i = lastEnd;
    else i = 0;
    int temp = cur.size();
    for (; i < n; i++) {
        vector<int> temp(cur[i]);
        temp.push_back(A[pos]);
        cur.push_back(temp);
    }
    return solve(A, cur, pos + 1, temp);
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

vector<vector<int>> Solution::subsetsWithDup(vector<int> &A) {
    sort(A.begin(), A.end());
    vector<vector<int>> output;
    
    output = solve(A, output, -1, 0);
    sort(output.begin(), output.end(), compareVectors);
    return output;
}
