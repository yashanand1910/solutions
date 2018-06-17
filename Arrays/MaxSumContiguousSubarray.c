/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer
 */
int max (int a, int b) {
    if (a > b) return a;
    return b;
}
 
int maxSubArray(const int* A, int n1) {
    int maxSum = A[0], maxTillHere = A[0];
    
    int i;
    for (i = 1; i < n1; i++) {
        maxTillHere = max(A[i], maxTillHere + A[i]);
        maxSum = max(maxTillHere, maxSum);
    }
    
    return maxSum;
}