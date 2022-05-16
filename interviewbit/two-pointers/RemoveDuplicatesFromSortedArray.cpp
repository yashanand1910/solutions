int Solution::removeDuplicates(vector<int> &A) {
    int n = A.size();
    if (n < 2) return n;
    int i = 0, j = 0;
    while (j < n) {
        A[i] = A[j];
        if (A[j] == A[j + 1]) {
            j++;
            continue;
        }
        i++;
        j++;
    }
    return i;
}
