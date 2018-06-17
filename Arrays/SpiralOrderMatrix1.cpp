vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
    vector<int> out;
    
    int T = 0, R = A[0].size()-1, B = A.size()-1, L = 0;
    int dir = 0;
    
    while (T <= B && L <= R) {
        if (dir == 0) {
            for (int i = L; i <= R; i++) out.push_back(A[T][i]);
            T++;
        }
        if (dir == 1) {
            for (int i = T; i <= B; i++) out.push_back(A[i][R]);
            R--;
        }
        if (dir == 2) {
            for (int i = R; i >= L; i--) out.push_back(A[B][i]);
            B--;
        }
        if (dir == 3) {
            for (int i = B; i >= T; i--) out.push_back(A[i][L]);
            L++;
        }
        
        dir = (dir + 1) % 4;
    }
    
    return out;
}