int Solution::nchoc(int A, vector<int> &B) {
    priority_queue<int> heap;
    int chocsEaten = 0;
    
    if(B.size() == 0){
        return 0;
    }
    
    for (auto item : B) {
        heap.push(item);
    }
    
    while (A--) {
        chocsEaten = (chocsEaten + (heap.top() % 1000000007)) % 1000000007;
        heap.push(heap.top() / 2);
        heap.pop();
    }
    
    return chocsEaten % 1000000007;
}
