int Solution::pow(int x, int n, int d) {
    if (x == 0) return 0;
    if (n == 0) return 1 % d;
    if (n == 1) {
        if (x > 0) return x % d;
        else if (x < 0) return d + x;
    }
    
    if (n == 2) return ((long long int)x%d * (long long int)x%d) % d;
    
    if (n % 2 == 0) return pow(((long long int)x%d * (long long int)x%d) % d, n / 2, d);
    return ((long long int)pow(x%d, 1, d) * (long long int)pow(((long long int)x%d * (long long int)x%d) % d, (n - 1) / 2, d)%d);
}
