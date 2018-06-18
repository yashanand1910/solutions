int numberPossible(vector<int> &A, int B, int C, bool first) {
    if (C == 0) return 0;
    
    vector<int> digitsOfC; int temp = C, result = 0;
    while (temp > 0) {
        digitsOfC.push_back(temp % 10);
        temp /= 10;
    }

    if (B > digitsOfC.size()) {
        for (int i = 0; i < (B - digitsOfC.size()); i++) {
            digitsOfC.push_back(0);
        }
    }
    
    if (B < digitsOfC.size()) {
        for (auto num : A) {
            if (num == 0 && B > 1) continue;
            result += pow(A.size(), B - 1);
        }
        return result;
    }
    
    for (auto num : A) {
        if (num == 0 && first && B > 1) continue;
        if (num < digitsOfC[digitsOfC.size() - 1]) {
            result += pow(A.size(), digitsOfC.size() - 1);
        }
        if (num == digitsOfC[digitsOfC.size() - 1]) {
            C = C % (int)pow(10, digitsOfC.size() - 1);
            result += numberPossible(A, B - 1, C, false);
        }
    }
    
    return result;
}

int Solution::solve(vector<int> &A, int B, int C) {
    if (A.size() == 0) return 0;
    
    return numberPossible(A, B, C, true);
}