int binSearch (const vector<int> &A, int B, bool searchFirst) {
    int low = 0, high = A.size() - 1, mid, result = -1;
    
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (A[mid] == B) {
            result = mid;
            if (searchFirst) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        else if (A[mid] < B) {
            low = mid + 1;
        }
        else {
            high = mid - 1;
        }
    }
    
    return result;
}

int Solution::findCount(const vector<int> &A, int B) {
    int firstIndex = binSearch(A, B, true);
    int lastIndex = binSearch(A, B, false);
    
    if (firstIndex == -1) return 0;
    
    return (lastIndex - firstIndex + 1);
}
