bool isSafe(int row, int col, vector<string> &board) {
    int i = 0, j;
    while (i < board.size()) {
        if (board[i][col] == 'Q') return false;
        i++;
    }
    i = row; j = col;
    while (i >= 0 && j >= 0) {
        if (board[i][j] == 'Q') return false;
        i--; j--;
    }
    i = row; j = col;
    while (i < board.size() && j < board.size()) {
        if (board[i][j] == 'Q') return false;
        i++; j++;
    }
    i = row; j = col;
    while (i < board.size() && j >= 0) {
        if (board[i][j] == 'Q') return false;
        i++; j--;
    }
    i = row; j = col;
    while (i >= 0 && j < board.size()) {
        if (board[i][j] == 'Q') return false;
        i--; j++;
    }
    
    return true;
}

vector<vector<string>> solve(vector<string> board, int row) {
    vector<vector<string>> output;
    if (row == board.size()) {
        output.push_back(board);
        return output;
    }

    for (int i = 0; i < board.size(); i++) {
        if (isSafe(row, i, board)) {
            vector<string> newBoard = board;
            newBoard[row][i] = 'Q';
            vector<vector<string>> temp = solve(newBoard, row + 1);
            if (temp.size() > 0) output.insert(output.end(), temp.begin(), temp.end());
        }
    }
    
    return output;
}

vector<vector<string> > Solution::solveNQueens(int A) {
    vector<vector<string>> output;
    
    vector<string> board;
    string temp = "";
    for (int i = 0; i < A; i++) temp += ".";
    for (int i = 0; i < A; i++) board.push_back(temp);
    
    output = solve(board, 0);
    
    return output;
}
