bool isPalindrome(string A) {
    if (A.size() <= 1) return true;
    return (A[0] == A[A.size() - 1] && isPalindrome(A.substr(1, A.size() - 2)));
}

vector<vector<string>> Solution::partition(string A) {
    vector<vector<string>> output;
    if (A.size() <= 1) {
        vector<string> temp;
        if (A.size() == 1) temp.push_back(A);
        output.push_back(temp);
        return output;
    }
    int len = 1;
    while (len <= A.size()) {
        string cur = A.substr(0, len);
        if (isPalindrome(cur)) {
            vector<vector<string>> temp = partition(A.substr(len, A.size() - len));
            for (int i = 0; i < temp.size(); i++) {
                temp[i].insert(temp[i].begin(), cur);
            }
            output.insert(output.end(), temp.begin(), temp.end());
        }
        len++;
    }
    return output;
}
