int Solution::search(const vector<int> &A, int B) {
    int low = 0, high = A.size() - 1, mid, pivot, prev, next;
    
    if (A[low] < A[high]) pivot = low;
    else {
        while (low <= high) {
            mid = low + (high - low) / 2;
            next = (mid + 1) % A.size();
            prev = (mid + A.size() - 1) % A.size();
            
            if (A[prev] > A[mid] && A[next] > A[mid]) {
                pivot = mid;
                break;
            }
            if (A[mid] <= A[high]) high = mid - 1;
            else if (A[mid] >= A[low]) low = mid + 1;
        }
    }
    
    low = pivot; int len = A.size() - 1;
    high = (pivot + A.size() - 1) % A.size();
    
    while (((low + A.size() - pivot)%A.size()) <= ((high + A.size() - pivot)%A.size())) {
        mid = (low + len / 2) % A.size();
        
        if (A[mid] == B) return mid;
        else if (A[mid] > B) {
            high = (mid + A.size() - 1) % A.size();
            len /= 2;
        } else {
            low = (mid + 1) % A.size();
            len /= 2;
        }
    }
    
    return -1;
}
