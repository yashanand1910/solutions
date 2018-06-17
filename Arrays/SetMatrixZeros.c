/**
 * @input A : 2D integer array 
 * @input n11 : Integer array's ( A ) rows
 * @input n12 : Integer array's ( A ) columns
 * 
 * @Output Void. Just modifies the args passed by reference 
 */
void setZeroes(int** A, int n11, int n12) {
    int i, j;
    int r[n11];
    int c[n12];
    for (i = 0; i < n11; i++) {
        r[i] = 1;
    }
    for (i = 0; i < n12; i++) {
        c[i] = 1;
    }
    
    for (i = 0; i < n11; i++) {
        for (j = 0; j < n12; j++) {
            if (A[i][j] == 0) {
                r[i] = 0;
                c[j] = 0;
            }
        }
    }
    
    for (i = 0; i < n11; i++) {
        if (r[i] == 0) {
            for (j = 0; j < n12; j++) {
                A[i][j] = 0;
            }
        }
    }
    for (i = 0; i < n12; i++) {
        if (c[i] == 0) {
            for (j = 0; j < n11; j++) {
                A[j][i] = 0;
            }
        }
    }
    
    return A;
}