int Solution::titleToNumber(string A) {
    vector<int> numberArr; int a;
    
    for (int i = 0; i < A.size(); i++) {
        a = (int) A[i];
        numberArr.push_back(a - 64);
    }

    int number = 0;
    for (int i = 0; i <= numberArr.size() - 1; i++) {
        number += pow(26, numberArr.size() - i - 1) * numberArr[i];
    }
    
    return number;
}
