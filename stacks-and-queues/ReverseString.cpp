stack<char> list;

string Solution::reverseString(string A) {
    string rev;
    for (int i = 0; i < A.size(); i++) {
        list.push(A[i]);
    }
    for (int i = 0; i < A.size(); i++) {
        rev += list.top();
        list.pop();
    }
    
    return rev;
}
