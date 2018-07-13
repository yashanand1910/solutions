bool compareVectors (vector<int> a, vector<int> b) {
    if (a.size() == 0) return true;
    if (b.size() == 0) return false;
    if (a[0] < b[0]) return true;
    else if (a[0] > b[0]) return false;
    else {
        int i = 0;
        while (a[i] == b[i] && i < a.size() - 1 && i < b.size() - 1) i++;
        if (a[i] < b[i]) return true;
        else if (a[i] > b[i]) return false;
        else return a.size() < b.size();
    }
}

vector<vector<int> > Solution::fourSum(vector<int> &A, int B) {
    vector<vector<int>> output;
    if (A.size() <= 4) return output;
    
    sort(A.begin(), A.end());
    
    unordered_map<int, int> table;
    
    for (int k = 1; k <= A.size() - 2; k++) {
        for (int i = 0; i < A.size() - 2 - k; i++) {
            int j = i + k;
            int low = j + 1, high = A.size() - 1;
            
            while (low < high) {
                if (A[i] + A[j] + A[low] + A[high] == B) {
                    output.push_back({A[i], A[j], A[low], A[high]});
                    high--;
                }
                else if (A[i] + A[j] + A[low] + A[high] > B) high--;
                else low++;
            }
        }
    }
    
    sort(output.begin(), output.end(), compareVectors);
    output.erase( unique( output.begin(), output.end() ), output.end() );
    return output;
}
