/**
 * @input A : 2D integer array 
 * @input n11 : Integer array's ( A ) rows
 * @input n12 : Integer array's ( A ) columns
 * 
 * @Output Void. Just modifies the args passed by reference 
 */
void rotate(int** A, int n11, int n12) {
    int end = n11 - 1, start = 0, temp, i;
    
    while (start < end) {
        
        for (i = 0; i < (end - start); i++) {
            temp = A[end - i][start];
            A[end - i][start] = A[end][end - i];
            A[end][end - i] = A[start + i][end];
            A[start + i][end] = A[start][start + i];
            A[start][start + i] = temp;
        }
        start++;
        end--;
    }
    
    return A;
}