string reverseString (string s) {
    char temp;
    for (int i = 0; i < s.size() / 2; i++) {
        temp = s[i];
        s[i] = s[s.size() - i - 1];
        s[s.size() - i - 1] = temp;
    }
    
    return s;
}

int Solution::reverse(int A) {
    bool isNegative = A < 0;
    try {
        if (isNegative) {
            return stoi("-" + reverseString(to_string(0 - A)));
        }
        else return stoi(reverseString(to_string(A)));
    } catch (out_of_range e) {
        return 0;
    }
}
