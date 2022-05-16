int Solution::coverPoints(vector<int> &A, vector<int> &B) {
    int minSteps = 0, x = A[0], y = B[0];
    
    for (int i = 1; i < A.size(); i++) {
        int a = A[i], b = B[i];
        
        minSteps += min(abs(b - y) + abs(a - x), max(abs(a - x), abs(b - y)));
        
        x = a; y = b;
    }
    
    return minSteps;
}
