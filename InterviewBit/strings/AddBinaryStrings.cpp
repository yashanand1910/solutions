string max (string A, string B) {
    if (A.size() > B.size()) return A;
    return B;
}
string min (string A, string B) {
    if (A.size() > B.size()) return B;
    return A;
}

string Solution::addBinary(string A, string B) {

    string s1, s2;
    s1 = max(A, B);
    s2 = min(A, B);
    int len = s1.size() - s2.size();

    for (int i = 0; i < len; i++) {
        s2 = "0" + s2;
    }

    vector<int> output; int carry = 0; string str = "";
    for (int i = s1.size() - 1; i >= 0; i--) {
        output.push_back(((int)s1[i] + (int)s2[i] + carry - 96) % 2);
        carry = ((int)s1[i] + (int)s2[i] + carry - 96) / 2;
        if (i == 0 && carry > 0) output.push_back(carry);
    }
    
    reverse(output.begin(), output.end());
    for (int i = 0; i < output.size(); i++) {
        str += to_string(output[i]);
    }
    return str;
}