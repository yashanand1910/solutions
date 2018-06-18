int Solution::isPrime(int A) {
    if (A == 2) return 1;
    if (A == 1) return 0;
    
    bool isPrime = true;
    for (int i = 2; i <= sqrt(A); i++) {
        if (A % i == 0) {
            isPrime = false;
            break;
        }
    }
    
    if (isPrime) return 1;
    return 0;
}