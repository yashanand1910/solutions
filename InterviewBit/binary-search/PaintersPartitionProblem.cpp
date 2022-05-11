int noOfPainters (vector<int> &boards, int maxTime) {
    int count = 0, sum = 0, i = 0;
    while (i < boards.size()) {
        if (boards[i] > maxTime) return INT_MAX;
        if (sum + boards[i] >= maxTime) {
            count++;
            if (sum + boards[i] == maxTime) i++;
            sum = 0;
        } else {
            if (i == boards.size() - 1) count++;
            sum += boards[i];
            i++;
        }
    }
    return count;
}

int Solution::paint(int A, int B, vector<int> &C) {
    if (A > C.size()) A = C.size();
    
    int sum = 0, max = INT_MIN;
    for (int i = 0; i < C.size(); i++) {
        if (C[i] > max) max = C[i];
        sum += C[i];
    }
    
    int low = max, high = sum, mid, midValue, midValueMinusOne;
    
    while (low <= high) {
        mid = low + (high - low) / 2;
        midValue = noOfPainters(C, mid);
        midValueMinusOne = noOfPainters(C, mid - 1);
        
        if (midValueMinusOne == INT_MAX) return ((long long int)B * max)%10000003;
        if (midValueMinusOne > midValue && midValue == A) return ((long long int)B * mid)%10000003;
        if (midValue <= A) high = mid - 1;
        else low = mid + 1;
    }
}
