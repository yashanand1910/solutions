vector<int> solve(vector<int> arr, int B) {
    if (arr.size() == 1 || B == 1) return arr;
    int i = 1, n = 1;
    while (n < B) {
        n *= ++i;
    }
    int m = n / i;
    while (i == arr.size()) {
        int j = 1;
        while(arr[j] <= arr[0]) j++;
        int temp = arr[0];
        arr[0] = arr[j];
        arr[j] = temp;
        B -= m;
        if (B <= m) {
            i--;
        }
    }
    vector<int> rem; int j = 0;
    for (; j < arr.size() - i; j++) {
        rem.push_back(arr[j]);
    }
    vector<int> arrNew;
    for (; j < arr.size(); j++) {
        arrNew.push_back(arr[j]);
    }
    vector<int> temp = solve(arrNew, B);
    rem.insert(rem.end(), temp.begin(), temp.end()); 
    
    return rem;
}

string Solution::getPermutation(int A, int B) {
    string output;
    vector<int> arr;
    for (int i = 1; i <= A; i++) {
        arr.push_back(i);
    }
    
    arr = solve(arr, B);
    
    for (int i = 0; i < arr.size(); i++) {
        output += to_string(arr[i]);
    }
    return output;
}
