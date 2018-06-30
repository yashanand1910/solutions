vector<vector<int> > Solution::threeSum(vector<int> &A) {
    vector<vector<int>> output;
    if (A.size() < 3) return output;
    int low, high;
    sort(A.begin(), A.end());
    for (int i = 0; i < A.size() - 2; i++) {
        low = i + 1;
        high = A.size() - 1;
        while (low < high) {
            if (A[i] + A[low] + A[high] == 0) {
                vector<int> temp{A[i], A[low], A[high]};
                if (find(output.begin(), output.end(), temp) == output.end()) {
                    output.push_back(temp);
                }
                low++;
            } else if (A[i] + A[low] + A[high] > 0) high--;
            else low++;
        }
    }
    
    return output;
}
