void Solution::merge(vector<int> &A, vector<int> &B) {
    int j = 0;
    for (int i = 0; i < B.size(); i++) {
        for (; j < A.size(); j++) {
            if (B[i] <= A[j]) {
                A.insert(A.begin() + j, B[i]);
                break;
            }
            if (j == A.size() - 1) {
                A.insert(A.end(), B[i]);
                break;
            }
        }
    }
}
