int uniquePaths(int A, int B) {
    if (A == 1 || B == 1) return 1; // Single row/column grids have a unique path
    
    return uniquePaths (A - 1, B) + uniquePaths (A, B - 1); // Problem can be divided into 2 parts for every grid
}
