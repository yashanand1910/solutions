void Solution::reverseWords(string &A) {
    vector<string> arr;
    arr.push_back("");
    int i = 0, k = 0;
    while (A[k] != '\0') {
        if (A[k] == ' ') {
            k++;
            arr.push_back("");
            continue;
        }
        arr[arr.size() - 1] += A[k];
        k++;
    }
    
    A = "";
    
    for (int i = arr.size() - 1; i >= 0; i--) {
        A += arr[i];
        if (i > 0) A += " ";
    }
    
}
