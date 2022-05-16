vector<int> Solution::order(vector<int> &A, vector<int> &B) {
    multimap<int, int> minHeap;
    for (int i = 0; i < A.size(); i++) minHeap.insert({A[i], B[i]});
    
    vector<int> sol(A.size(), INT_MIN);
    multimap<int, int>::iterator it = minHeap.begin();
    
    while (it != minHeap.end()) {
        int i = 0, n = it->second;
        while (n) {
            if (sol[i] == INT_MIN) n--;
            i++;
        }
        while (sol[i] != INT_MIN) i++;
        sol[i] = it->first;
        it++;
    }
    
    return sol;
}
