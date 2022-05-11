/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer array. You need to malloc memory, and fill the length in len1
 */
int compareInteger(const void* a, const void* b) {
    int value1 = *((int*) a);
    int value2 = *((int*) b);
    if (value1 > value2) return 1;
    return 0;
}
 
int* wave(int* A, int n1, int *len1) {
    *len1 = n1;
    
    qsort(A, n1, sizeof(int), compareInteger);
    
    int i = 0;
    while (i < n1) {
        if (i == n1 - 1)
        int temp = A[i];
        A[i] = A[i + 1];
        A[i + 1] = temp;
        i += 2;
    }
    
    return A;
}
