int Solution::atoi(const string A) {
    long long int output = 0; bool numberFound = false, minusFound = false;
    vector<int> num;
    for (int i = 0; i < A.size(); i++) {
        if (!numberFound && A[i] == ' ') continue;
        if (A[i] == '-') {
            minusFound = true;
            numberFound = true;
            continue;
        }
        if (A[i] == '+') {
            numberFound = true;
            continue;
        }
        numberFound = true;
        if (A[i] == ' ' || int(A[i]) < 48 || int(A[i]) > 57) break;
        num.push_back(int(A[i]) - 48);
    }

    long long int i = 0, ten = pow(10, num.size() - 1);
    while(i < num.size()) {
        output += num[i] * ten;
        if (minusFound) {
            if ((-1)*output <= INT_MIN) return INT_MIN;
        } else {
            if (output >= INT_MAX) return INT_MAX;
        }
        ten /= 10;
        i++;
    }
    
    if (minusFound) return (-1)*output;
    return output;
}
