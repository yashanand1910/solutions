/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Integer
 * 
 * @Output Integer array. You need to malloc memory, and fill the length in len1
 */
int* rotateArray(int* A, int n1, int B, int *len) {
    int *ret = (int *)malloc(n1 * sizeof(int));
    *len = n1;
    int i;
    for (i = 0; i < n1; i++) ret[i] = A[(i + B)%(*len)];

    return ret;
}