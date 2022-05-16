stack<string> list;

int Solution::evalRPN(vector<string> &A) {
    int temp, i = 0;
    list.push(to_string(0));
    
    while (i < A.size()) {
        if (A[i] == "+") {
            temp = stoi(list.top());
            list.pop();
            temp = temp + stoi(list.top());
            list.pop();
            list.push(to_string(temp));
        } else if (A[i] == "-") {
            temp = stoi(list.top());
            list.pop();
            temp = stoi(list.top()) - temp;
            list.pop();
            list.push(to_string(temp));
        } else if (A[i] == "*") {
            temp = stoi(list.top());
            list.pop();
            temp = temp * stoi(list.top());
            list.pop();
            list.push(to_string(temp));
        } else if (A[i] == "/") {
            temp = stoi(list.top());
            list.pop();
            temp = stoi(list.top()) / temp;
            list.pop();
            list.push(to_string(temp));
        } else {
            list.push(A[i]);
        }
        i++;
    }
    
    return stoi(list.top());
}
