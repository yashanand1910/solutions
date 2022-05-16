int Solution::singleNumber(const vector<int> &A) {
    int out = A[0];
    for (int i = 1; i < A.size(); i++) {
        out ^= A[i];
    }
    
    return out;
}
