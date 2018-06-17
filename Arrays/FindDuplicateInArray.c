/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer
 */
 
int repeatedNumber(const int* A, int n1) {
    int slow = A[0];
    int fast = A[slow];
    
    while(slow != fast) {
        slow = A[slow];
        fast = A[A[fast]];
    }
    
    slow = 0;
    while(slow != fast) {
        slow = A[slow];
        fast = A[fast];
    }
    
    return slow;
}
