vector<vector<int> > Solution::squareSum(int A) {
    vector<vector<int> > ans;
    for (int a = 0; a * a < A; a++) {
        for (int b = 0; b <= a; b++) {
            if (a * a + b * b == A) {
                vector<int> newEntry; 
                newEntry.push_back(b);
                newEntry.push_back(a);
                ans.push_back(newEntry);
            }
        }
    }
    return ans;
}
