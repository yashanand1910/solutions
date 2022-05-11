string reverse (string s) {
    char temp;
    for (int i = 0; i < s.size() / 2; i++) {
        temp = s[i];
        s[i] = s[s.size() - i - 1];
        s[s.size() - i - 1] = temp;
    }
    
    return s;
}

int Solution::isPalindrome(int A) {
    string s = to_string(A);
    if (s == reverse(s)) return 1;
    return 0;
}
