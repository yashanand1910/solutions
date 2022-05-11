int Solution::diffPossible(const vector<int> &A, int B) {
    unordered_map<int, int> table;
    for (int i = 0; i < A.size(); i++) {
        if (table.find(A[i]) != table.end()) return 1;
        table.insert({A[i] + B, A[i] + B});
        // table.insert({B - A[i], B - A[i]});
    }
    
    return 0;
}
