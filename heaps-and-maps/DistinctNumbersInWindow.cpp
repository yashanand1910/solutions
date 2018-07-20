vector<int> Solution::dNums(vector<int> &A, int B) {
    vector<int> output;
    if (B > A.size()) return output;
    
    unordered_map<int, int> m;
    int i = 0, j;
    for (j = 0; j < B; j++) {
        if (m.find(A[j]) != m.end()) m[A[j]]++;
        else m.insert({A[j], 1});
    }
    j--;
    output.push_back(m.size());
    
    while (j < A.size() - 1) {
        i++; j++;
        if (m[A[i - 1]] == 1) m.erase(A[i - 1]);
        else m[A[i - 1]]--;
        if (m.find(A[j]) != m.end()) m[A[j]]++;
        else m.insert({A[j], 1});
        
        output.push_back(m.size());
    }
    
    return output;
}
