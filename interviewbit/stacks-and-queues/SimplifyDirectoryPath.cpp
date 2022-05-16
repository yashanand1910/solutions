stack<string> list;

string Solution::simplifyPath(string A) {
    bool found = false; int i = 0; string temp, output;
    while (i < A.size()) {
        while (A[i] != '/' && i < A.size()) {
            temp += A[i];
            i++;
        }
        if (temp != "." && temp != ".." && temp != "") {
            list.push(temp);
        } else if (temp == "..") {
            if (list.size() > 0) list.pop();
        }
        found = false;
        temp = "";
        if (!found && A[i] =='/') {
            found = true;
            i++;
        }
    }
    
    if (list.size() == 0) output = "/";
    while (list.size() > 0) {
        output = "/" + list.top() + output;
        list.pop();
    }
    
    return output;
}
