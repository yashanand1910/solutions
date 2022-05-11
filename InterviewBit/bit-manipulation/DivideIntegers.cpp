int Solution::divide(int a, int b) {
    
   long long n = a, m = b;
   int sign = n < 0 ^ m < 0 ? -1 :1;
   long long q = 0;
   n = abs(n);
   m = abs(m);
   for (long long t = 0, i = 31; i >= 0; i--)
        if (t + (m << i) <= n)
            t += m << i, q |= 1LL << i;

    // assign back the sign
    if (sign < 0) q = -q;

    // check for overflow and return
    return q >= INT_MAX || q < INT_MIN ? INT_MAX : q;
}
