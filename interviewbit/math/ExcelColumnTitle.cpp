string Solution::convertToTitle(int A) {
    string s; int C;
    while (A > 0) {
        s = char(65 + ((A - 1) % 26)) + s;
        A = (A - 1) / 26;
    }
    
    return s;
}
