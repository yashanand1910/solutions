int Solution::findMin(const vector<int> &A) {
    int low = 0, high = A.size() - 1, mid, prev, next;
    
    while (low <= high) {
        mid = low + (high - low) / 2;
        prev = (mid + A.size() - 1) % A.size();
        next = (mid + 1) % A.size();
        if (A[low] <= A[high]) return A[low];
        else if (A[prev] >= A[mid] && A[mid] <= A[next]) return A[mid];
        else if (A[low] <= A[mid]) low = mid + 1;
        else if (A[high] >= A[mid]) high = mid - 1;
    }
    
    return -1;
}
