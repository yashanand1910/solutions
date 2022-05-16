bool isPrime (int num) {
    bool is = true;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            is = false;
            break;
        }
    }
    return is;
}

vector<int> Solution::sieve(int A) {
    vector<int> primesTillA;
    if (A == 1) return primesTillA;
    if (A >= 2) {
        primesTillA.push_back(2);
    }
    if (A == 2) return primesTillA;
    
    for(int i = 3; i <= A; i++) {
        if (isPrime(i)) primesTillA.push_back(i);
    }
    
    return primesTillA;
}