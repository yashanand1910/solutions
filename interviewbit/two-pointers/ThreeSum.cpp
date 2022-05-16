int Solution::threeSumClosest(vector<int> &A, int B) {
    int diff = INT_MAX, sum, low, high;
    sort(A.begin(), A.end());
    for (int i = 0; i < A.size() - 2; i++) {
        low = i + 1;
        high = A.size() - 1;
        while (high > low) {
            if (abs(B - (A[i] + A[low] + A[high])) < diff) {
                sum = A[i] + A[low] + A[high];
                diff = abs(B - sum);
            }
            if (A[low] + A[high] + A[i] == B) return B;
            else if (A[low] + A[high] + A[i] > B) high--;
            else if (A[low] + A[high] + A[i] < B) low++;
        }
    }
    return sum;
}