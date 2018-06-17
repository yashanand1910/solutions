/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output Integer
 */
 struct Number {
     int num;
     int count;
 };
 
int repeatedNumber(const int* A, int n1) {
    struct Number list[2];
    list[0].num = 0;
    list[1].num = 0;
    list[0].count = 0;
    list[1].count = 0;
    int n = n1 / 3;
    
    int i = 0, j;
    while (i < n1) {
        if (list[0].num == A[i] || list[1].num == A[i]) {
            if (list[0].num == A[i]) list[0].count++;
            else if (list[1].num == A[i]) list[1].count++;
        } else if (list[0].count == 0 || list[1].count == 0) {
            if (list[0].count == 0) {
                list[0].num = A[i];
                list[0].count = 1;
            }
            else if (list[1].count == 0) {
                list[1].num = A[i];
                list[1].count = 1;
            }
        } else {
            list[0].count--;
            list[1].count--;
        }
        i++;
    }
    
    int count;
    for (i = 0; i < 2; i++) {
        count = 0;
        for (j = 0; j < n1; j++) {
            if (list[i].num == A[j]) count++;
            if (count > n) return list[i].num;
        }
    }
    
    return -1;
    
}