stack<int> list;

int Solution::largestRectangleArea(vector<int> &A) {
    int h, l, r, maxArea = 0;
    
    list.push(0);
    
    for (int i = 1; i < A.size(); i++) {
        if (A[list.top()] < A[i]) {
            list.push(i);
        } else {
            while (list.size() > 0 && A[i] < A[list.top()]) {
                h = A[list.top()];
                list.pop();
                if (list.size() == 0) l = -1;
                else l = list.top();
                r = i;
                maxArea = max(maxArea, h * (r - l - 1));
            }
            list.push(i);
        }
    }
    r = A.size();
    while (list.size() > 0) {
        h = A[list.top()];
        list.pop();
        if (list.size() == 0) l = -1;
        else l = list.top();
        maxArea = max(maxArea, h * (r - l - 1));
    }
    
    return maxArea;
}
