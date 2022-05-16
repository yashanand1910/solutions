int Solution::maxArea(vector<int> &A) {
    if (A.size() < 2) {
        return 0;
    }
    long long int maxVol = INT_MIN, low, high;
    low = 0;
    high = A.size() - 1;
    while (low < high) {
        maxVol = max(maxVol, (long long int)(high - low)*(long long int)min(A[low], A[high]));
        if (A[low] <= A[high]) {
            low++;
        } else high--;
    }
    
    return maxVol;
}
