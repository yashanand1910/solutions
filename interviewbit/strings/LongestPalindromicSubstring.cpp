bool isPalindromic(string A) {
    if (A.size() == 1) return true;
    if (A.size() == 2 && A[0] == A[A.size() - 1]) return true;
    return (A[0] == A[A.size() - 1]) && isPalindromic(A.substr(1, A.size() - 2));
}

string Solution::longestPalindrome(string A) {
    int n = A.size();
    
    while(n > 0) {
        for (int i = 0; i <= A.size() - n; i++) {
            if(isPalindromic(A.substr(i, n))) return A.substr(i, n);
        }
        n--;
    }
}
