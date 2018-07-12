int Solution::Mod(int A, int B, int C) {
    if (B == 0) return 1 % C;
    if (B == 1) {
        if (A >= 0) return A % C;
        return C + A;
    }
    if (B == 2) {
        return ((long long int)A * (long long int)A) % C;
    }
    if (B % 2 == 0) return ((long long int)Mod(A, B / 2, C) * (long long int)Mod(A, B / 2, C)) % C;
    return ((long long int)Mod(A, 1, C) * (long long int)(((long long int)Mod(A, B / 2, C) * (long long int)Mod(A, B / 2, C)) % C)) % C;
}
