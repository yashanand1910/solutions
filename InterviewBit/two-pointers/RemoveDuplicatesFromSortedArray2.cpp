int Solution::removeDuplicates(vector<int> &A) {
    if (A.size() < 2) return A.size();
    int i = 0, j, count = 0;
    while (j < A.size()) {
        if (A[j] != A[i]) {
            count = 0;
            i++;
            A[i] = A[j];
            continue;
        }
        j++;
        if (A[j] == A[i] && count == 0 && j < A.size()) {
            i++;
            A[i] = A[j];
            count++;
        }
    }
    return i + 1;
}
