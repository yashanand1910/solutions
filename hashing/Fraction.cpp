string Solution::fractionToDecimal(int a, int b) {
    long long A = (long long) a;
    long long B = (long long) b;
    string sol = "";
    sol += to_string(A / B);
    if (sol == "0" && ((A < 0 && B > 0) || (A > 0 && B < 0))) sol = "-" + sol;
    A = abs(A);
    B = abs(B);
    if (!(A %= B)) return sol;
    
    unordered_map<long long, long long> list;
    sol += ".";
    string temp = "";
    int i = 0;
    while(true) {
        A *= 10;
        if (list.find(A) != list.end()) {
            return sol + temp.substr(0, list[A]) + "(" + temp.substr(list[A], temp.length() - list[A]) + ")";
        }
        list.insert({A, i++});
        temp += to_string(A / B);
        if (!(A %= B)) return sol + temp;
    }
}
