vector<int> Solution::slidingMaximum(const vector<int> &A, int B) {
    deque<int> list(B);
    vector<int> maxes;
    int i = 0;
    for (; i < B; i++) {
        while (!list.empty() && A[i] > A[list.back()]) {
            list.pop_back();
        }
        list.push_back(i);
    }
    maxes.push_back(A[list.front()]);
    for(; i < A.size(); i++) {
        while (!list.empty() && list.front() <= i - B) {
            list.pop_front();
        }
        while (!list.empty() && A[i] > A[list.back()]) {
            list.pop_back();
        }
        list.push_back(i);
        maxes.push_back(A[list.front()]);
    }
    
    return maxes;
}
