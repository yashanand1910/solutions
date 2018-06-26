int Solution::cntBits(vector<int> &A) {
    long long int sum = 0, count;
    for (int i = 0; i < 32; i++) {
        long long int count = 0;
        for (int j = 0; j < A.size(); j++) {
            if (A[j] & (1 << i)) count++;
        }
        sum += count * (A.size() - count) * 2;
    }
    
    return sum % (long long int) (pow(10, 9) + 7);
}
