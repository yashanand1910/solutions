void Solution::arrange(vector<int> &A) {
    int N = A.size();
    for (int i = 0; i < A.size(); i++) {
        if ((int)(A[A[i]] / N) == 0) A[i] = ((A[i] + 1) * N) + A[A[i]];
        else A[i] = ((A[i] + 1) * N) + (((int)(A[A[i]] / N)) - 1);
    }
    for (int i = 0; i < A.size(); i++) {
        A[i] = (int)A[i] % N;
    }
}