int Solution::sqrt(int A) {
    if (A == 0 || A == 1) return A;
    
    int start = 1;
    int end = A;
    int ans;
    long int mid;
    
    while (start <= end) {
        mid = (long int)start + (end - start) / 2;

        if (pow(mid, 2) == A) return mid;
        else if (pow(mid, 2) > A) {
            end = mid - 1;
        }
        else {
            start = mid + 1;
            ans = mid;
        }
    }
    return ans;
}
