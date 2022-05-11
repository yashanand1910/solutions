string Solution::convert(string A, int B) {
    if (B == 1) return A;
    
    int i = 0, k = 0, temp, j; string str = "";
    while (i < B) {
        k = i; j = 1;
        while(k < A.size()) {
            str += A[k];
            if (B == 1) break;
            if (i % (B - 1) == 0) k += (2 * B) - 2;
            else {
                temp = 2 * i * pow(-1, j);
                k += ((2 * B) - 2) * (j % 2) + temp;
                j++;
            }
        }
        i++;
    }
    return str;
}