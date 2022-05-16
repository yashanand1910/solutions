void solve (vector<string> &output, vector<string> &container, vector<string> &collection, string A) {
    if (A.size() == 0) {
        output = container;
        return;
    }
    
    string str = collection[stoi(A.substr(A.size() - 1, 1))];
    A = A.substr(0, A.size() - 1);
    vector<string> temp;
    
    for (int i = 0; i < str.size(); i++) {
        for(int j = 0; j < container.size(); j++) {
            temp.push_back(str[i] + container[j]);
        }
    }

    solve (output, temp, collection, A);
}

vector<string> Solution::letterCombinations(string A) {
    vector<string> output, container;
    
    vector<string> collection = {
        "0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    container.push_back("");
    solve(output, container, collection, A);
    
    return output;
}
