void Solution::sortColors(vector<int> &A) {
    vector<int> index(3, 0);
    for (int j = 0; j < A.size(); j++) {
        index[A[j]]++;
    }
    int k = 0, i = 0;
    while (i < A.size()) {
        for (int j = 0; j < index[k]; j++) {
            A[i] = k;
            i++;
        }
        k++;
    }
}
