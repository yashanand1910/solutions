int binarySearch(const vector<int> &A, int B, bool searchFirst) {
    int low = 0, high = A.size() - 1, mid, index = -1;
    
    while (low <= high) {
        mid = low + (high - low) / 2;
        if (A[mid] == B) {
            index = mid;
            if (searchFirst) high = mid - 1;
            else low = mid + 1;
        } else if (A[mid] < B) low = mid + 1;
        else high = mid - 1;
    }
    
    return index;
}

vector<int> Solution::searchRange(const vector<int> &A, int B) {
    vector<int> range(2);
    range[0] = binarySearch(A, B, true);
    range[1] = binarySearch(A, B, false);
    
    return range;
}
