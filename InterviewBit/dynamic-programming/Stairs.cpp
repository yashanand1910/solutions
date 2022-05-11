int memo[100] = {0};

int Solution::climbStairs(int A) {
    if (A == 1 || A == 2) return A;
    
    if (memo[A - 1] == 0) memo[A - 1] = climbStairs(A - 1);
    if (memo[A - 2] == 0) memo[A - 2] = climbStairs(A - 2);
    
    return memo[A - 1] + memo[A - 2];
}
