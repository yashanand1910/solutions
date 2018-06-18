int Solution::gcd(int A, int B) {
    int mini = min(A, B);
    int maxi = max(A, B);
    
    if (mini == 0) return maxi;
    
    int i = 1;
    
    while (i <= mini) {
        if (maxi % (mini / i) == 0) return mini/i;
        i++;
        while (mini % i != 0) i++;
    }
}
