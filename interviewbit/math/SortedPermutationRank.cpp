long long int factorial (int n) {
    long long int fact = 1;
    if (n == 0) return fact;
    for(int i = 1; i <= n; i++) fact =(long long int)fact * i;
    return fact;
}

long long int findSubRank(string A) {
    if (A.size() == 1) return 1;
    
    string sorted = A;
    sort(sorted.begin(), sorted.end());
    
    return (long long int)(findSubRank(A.substr(1, A.size() - 1)) % 1000003 + ((long long int)sorted.find(A[0]) * (long long int)factorial(A.size() - 1)));
}

int Solution::findRank(string A) { 
    return (int)(findSubRank(A) % 1000003);
}
