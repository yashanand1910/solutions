vector<int> Solution::grayCode(int A) {
    vector<int> code;
    if (A == 1) {
        code = {0, 1};
        return code;
    }
    code = grayCode(A - 1);
    int n = code.size();
    for (int i = n - 1; i >= 0; i--) {
        code.push_back(pow(2, A - 1) + code[i]);
    }
    
    return code;
}
