int Solution::isValidSudoku(const vector<string> &A) {
    vector<unordered_map<int, int>> horTable(9), verTable(9), boxTable(9);
    
    
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (A[i][j] == '.') continue;
            int k = (i / 3)*3 + (j / 3);
            if (horTable[i].find(A[i][j]) != horTable[i].end() || verTable[j].find(A[i][j]) != verTable[j].end() || boxTable[k].find(A[i][j]) != boxTable[k].end()) {
                return 0;
            }
            horTable[i].insert({A[i][j], A[i][j]});
            verTable[j].insert({A[i][j], A[i][j]});
            boxTable[k].insert({A[i][j], A[i][j]});
        }
    }
    
    return 1;
}
