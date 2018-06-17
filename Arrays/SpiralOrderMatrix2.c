/**
 * @input A : Integer
 * 
 * @Output 2D int array. You need to malloc memory. Fill in len1 as row, len2 as columns 
 */
int ** generateMatrix(int A, int *len1, int *len2) {
    *len1 = A;
    *len2 = A;
    int** a = (int**)malloc(A * sizeof(int*)) ; 
    int i;
    for (i = 0; i < A; i++) {
        *(a + i) = (int*)malloc(A * sizeof(int));
    }
    
    int top = 0, left = 0, right =  A - 1, bottom = A - 1;
    int dir = 0, count = 0;
    while (top <= bottom && left <= right) {
        if (dir == 0) {
            for (i = left; i <= right; i++) {
                a[top][i] = ++count;
            }
            top++;
        }
        if (dir == 1) {
            for (i = top; i <= bottom; i++) {
                a[i][right] = ++count;
            }
            right--;
        }
        if (dir == 2) {
            for (i = right; i >= left; i--) {
                a[bottom][i] = ++count;
            }
            bottom--;
        }
        if (dir == 3) {
            for (i = bottom; i >= top; i--) {
                a[i][left] = ++count;
            }
            left++;
        }
        dir = (dir + 1) % 4;
    }
    
    return a;
}