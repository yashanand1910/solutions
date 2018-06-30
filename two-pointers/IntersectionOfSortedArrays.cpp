vector<int> Solution::intersect(const vector<int> &A, const vector<int> &B) {
    vector<int> output; int i, j;
    j = i = 0;
    while (j < A.size() && i < B.size()) {
        if (B[i] == A[j]) {
            output.push_back(B[i]);
            i++;
        }
        else if (B[i] < A[j]) {
            i++;
            continue;
        }
        j++;
    }
    
    return output;
}
