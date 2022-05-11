int Solution::braces(string A) {
    stack<char> list; int operationCount = 0;
    
    int i = 0;
    while (i < A.size()) {
        if (A[i] == '(') {
            list.push(A[i]);
            operationCount++;
        }
        else if (A[i] == ')') list.pop();
        else if (A[i] == '+' || A[i] == '*' || A[i] == '-' || A[i] == '/') {
            if (operationCount > 0) operationCount--;
        }                                   
        i++;
    }
    
    if (operationCount == 0) return 0;
    return 1;
}
