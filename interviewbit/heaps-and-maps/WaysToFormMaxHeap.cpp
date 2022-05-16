long long int fact(long long int i) {
    if (i < 2) return 1;
    return i * fact(i - 1);
}

int Solution::solve(int A) {
    if (A < 3) return 1;
    
    long long int h = log(A) / log(2);
    long long int m = pow(2, h);
    long long int p = A - (m - 1);
    long long int L;
    
    if (p >= m / 2) L = m - 1;
    else L = m - 1 - (m / 2 - p);
    
    return ((fact(A - 1) / (fact(A - 1 - L) * fact(L))) * solve(L) * solve(A - 1 - L)) % 1000000007;
}
