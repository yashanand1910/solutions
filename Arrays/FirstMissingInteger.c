/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer
 */
incrementCount(int* A, int* a, int n1) {
    int prev = *a;
    while (prev > 0 && prev <= n1) {
        int temp = prev;
        prev = A[prev - 1];
        A[temp - 1] = -1;
        a = &A[*a - 1];
    }
}
 
int firstMissingPositive(int* A, int n1) {
    int i, j;
    
    for(i = 0; i < n1; i++) {
        if (A[i] <= 0 || A[i] > n1) A[i] = 0;
    }
    for (i = 0; i < n1; i++) {
        if (A[i] != 0) {
            incrementCount(A, A + i, n1);
        }
    }
    
    int firstMissing = 1;
    for (i = 0; i < n1; i++) {
        if (A[i] == -1) firstMissing++;
        else break;
    }
    return firstMissing;
}
