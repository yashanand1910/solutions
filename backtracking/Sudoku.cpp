bool isSafe(int num, int row, int col, vector<vector<char>> &A) {
    int i = row, j = 0;
    while (j < 9) {
        if ('0' + num == A[i][j]) return false;
        j++;
    }
    i = 0, j = col;
    while (i < 9) {
        if ('0' + num == A[i][j]) return false;
        i++;
    }
    int boxRow = row / 3, boxCol = col / 3;
    i = boxRow * 3, j = boxCol * 3;;
    int m = i + 3, n = j + 3;
    while (i < m) {
        j = boxCol * 3;
        while (j < n) {
            if (A[i][j] == '0' + num) return false;
            j++;
        }
        i++;
    }
    
    return true;
}

vector<int> findNextHole(vector<vector<char> > &A) {
    int i = 0, j; bool found = false;
    while (i < 9) {
        j = 0;
        while (j < 9) {
            if (A[i][j] == '.') {
                found = true;
                break;
            };
            j++;
        }
        if (found) break;
        i++;
    }
    vector<int> holePos = {i, j};
    return holePos;
}

void Solution::solveSudoku(vector<vector<char> > &A) {
    vector<int> hole = findNextHole(A);
    for (int i = 1; i <= 9; i++) {
        if(isSafe(i, hole[0], hole[1], A)) {
            A[hole[0]][hole[1]] = '0' + i;
            vector<int> next = findNextHole(A);
            if (next[0] == 9) return;
            solveSudoku(A);
            if (next == findNextHole(A)) A[hole[0]][hole[1]] = '.';
            else break;
        }
    }
}
