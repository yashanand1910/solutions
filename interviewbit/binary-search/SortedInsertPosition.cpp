int max (int a, int b) {
    if (a > b) return a;
    return b;
}
int Solution::searchInsert(vector<int> &A, int B) {
    int low = 0, high = A.size() - 1, mid;
    
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (A[mid] == B) return mid;
        else if (A[mid] < B) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    return max(low, high);
}
