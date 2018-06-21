int Solution::isPalindrome(string A) {
    vector<char> arr;
    vector<char> rev;
    
    for (int i = 0; i < A.size(); i++) {
        if (isalnum(A[i])) arr.push_back(tolower(A[i]));
    }
    
    rev = arr;
    reverse(rev.begin(), rev.end());
    
    if (arr == rev) return 1;
    return 0;
}
