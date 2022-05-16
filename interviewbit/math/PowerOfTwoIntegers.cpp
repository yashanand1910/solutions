/**
 * @input A : Integer
 * 
 * @Output Integer
 */
int isPower(int A) {
    int i,a;
    double p;
    if(A == 1)
        return 1;
    for(a = 1;a <= sqrt(A);a++)
    {
        p = log(A) / log(a);
        if(p - (int)p < 0.000000001)
            return 1;
    }
    return 0;
}
