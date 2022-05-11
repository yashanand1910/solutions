/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Void. Just modifies the args passed by reference 
 */
int compareInteger (const void* a, const void* b) {
    if (*((int*)a) > *((int*)b)) return 1;
    return 0;
}
 
void nextPermutation(int* A, int n1) {
    int suffixStart = 0, i, temp;
    for (i = n1 - 1; i > 0; i--) {
        if (A[i] < A[i - 1]) continue;
        else {
            suffixStart = i;
            break;
        }
    }
    
    if (suffixStart == 0) {
        qsort(A, n1, sizeof(int), compareInteger);
        return;
    }
    
    for (i = 0; i < n1; i++) {
        if (A[suffixStart - 1] < A[n1 - 1 - i]) {
            temp = A[suffixStart - 1];
            A[suffixStart - 1] = A[n1 - 1 - i];
            A[n1 - 1 - i] = temp;
            break;
        }
    }

    for (i = 0; i < (n1 - suffixStart) / 2; i++) {
        temp = A[i + suffixStart];
        A[i + suffixStart] = A[n1 - i - 1];
        A[n1 - i - 1] = temp;
    }
    
    return;
}