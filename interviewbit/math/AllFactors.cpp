vector<int> Solution::allFactors(int A) {
    vector<int> factors;
    if (A == 1) factors.push_back(1);
    else {
        for (int i = 1; i <= sqrt(A); i++) {
            if (A % i == 0) {
                factors.push_back(i);
                if (i != sqrt(A)) factors.push_back(A / i);
            }
        }
    }
    
    sort(factors.begin(), factors.end());
    
    return factors;
}