int Solution::findMinXor(vector<int> &A) {
    int mini = INT_MAX;
    sort(A.begin(), A.end());
    
    for (int i = 0; i < A.size() - 1; i++) {
        mini = min (mini, A[i] ^ A[i + 1]);
    }

    return mini;
}
