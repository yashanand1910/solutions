stack<char> list;

int Solution::isValid(string A) {
    for (int i = 0; i < A.size(); i++) {
        if (list.size() == 0) {
            list.push(A[i]);
            continue;
        }
        if (list.top() == '(' && A[i] == ')') list.pop();
        else if (list.top() == '[' && A[i] == ']') list.pop();
        else if (list.top() == '{' && A[i] == '}') list.pop();
        else list.push(A[i]);
    }
    
    if (list.size() > 0) return 0;
    return 1;
}
