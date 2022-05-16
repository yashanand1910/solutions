/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer array. You need to malloc memory, and fill the length in len1
 */
int* repeatedNumber(const int* A, int n1, int *len1) {
    *len1 = 2;
    int* out = (int*)malloc(*len1 * sizeof(int));
    
    int i;
    long long sum = (long) n1 * (n1 + 1) / 2;
    long long sum2 = (long) n1 * (n1 + 1) * (2*n1 + 1) / 6;
    long long sumArr = 0;
    long long sum2Arr = 0;
    for (i = 0; i < n1; i++) {
        sumArr += (long long)A[i];
        sum2Arr += (long long)A[i]*A[i];
    }
    long long a2minusb2 = sum2Arr - sum2;
    long long aminusb = sumArr - sum;
    long long aplusb = a2minusb2 / aminusb;
    
    int a = (int) (aminusb + aplusb) / 2;
    int b = (int) aplusb - a;
    
    out[0] = a;
    out[1] = b;
    
    return out;
}