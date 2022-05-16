int noOfStudents (vector<int> &books, int maxPages) {
    int sum = 0, count = 0, i = 0;
    while (i < books.size()) {
        if (books[i] > maxPages) return INT_MAX;
        if (sum + books[i] >= maxPages) {
            count++;
            if (sum + books[i] == maxPages) i++;
            sum = 0;
        } else {
            if (i == books.size() - 1) count++;
            sum += books[i];
            i++;
        }
    }
    
    return count;
}

int Solution::books(vector<int> &A, int B) {
    if (B > A.size()) return -1;
    
    // return noOfStudents(A, 96);
    int max = INT_MIN, sum = 0; 
    for (auto pages : A) {
        if (pages > max) max = pages;
        sum += pages;
    }
    
    int low = max, high = sum, mid, midValue, midValueMinusOne;
    
    while(low <= high) {
        mid = low + (high - low) / 2;
        midValue = noOfStudents(A, mid);
        midValueMinusOne = noOfStudents(A, mid - 1);
        
        if (midValueMinusOne == INT_MAX) return mid;
        if (midValueMinusOne > midValue && midValue == B) return mid;
        if (midValue <= B) high = mid - 1;
        else if (midValue > B) low = mid + 1;
    }
}
