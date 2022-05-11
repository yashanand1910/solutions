int Solution::removeElement(vector<int> &A, int B) {
    int i, n = A.size();
    while (i < A.size()) {
        if (A[i] == B) break;
        i++;
    }
    
    if (i == A.size()) {
        return A.size();
    }
    
    int j = i + 1;
    while (j < A.size()) {
        if (A[j] != B) {
            A[i] = A[j];
            i++;
        }
        j++;
    }
    
    while (i < n) {
        A.pop_back();
        i++;
    }
    
    return A.size();
}
