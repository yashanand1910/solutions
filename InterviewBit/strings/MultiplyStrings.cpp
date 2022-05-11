string Solution::multiply(string A, string B) {
    if (A == "0" || B == "0") return "0";
    
    vector<int> num1, num2, output(A.size() * B.size() + 1, 0); int carry = 0; string str = "";
    for (int i = 0; i < A.size(); i++) {
        num1.push_back(int(A[i]) - 48);
    }
    for (int i = 0; i < B.size(); i++) {
        num2.push_back(int(B[i]) - 48);
    }
    
    
    int k = 0, l, temp;
    for (int i = num2.size() - 1; i >= 0; i--) {
        l = 0; carry = 0;
        for (int j = num1.size() - 1; j >= 0; j--) {
            temp = output[k + l];
            output[k + l] = (output[k + l] + (num2[i] * num1[j]) + carry) % 10;
            carry = (temp + (num2[i] * num1[j]) + carry) / 10;
            l++;
            if (j == 0) output[k + l] += carry;
        }
        k++;
    }
    
    reverse(output.begin(), output.end());
    int max = 0;
    for (int i = 0; i < output.size(); i++) {
        if (max == 0 && output[i] == 0) continue;
        max = 10;
        str += to_string(output[i]);
    }
    
    return str;
}
