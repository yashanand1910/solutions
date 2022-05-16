class compareNo {
public:
    bool operator()(pair<int, ListNode*> n1,pair<int, ListNode*> n2) {
        return n1.first > n2.first;
    }
};

ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, compareNo> heap;

    for (auto i : A) heap.push(make_pair(i->val, i));
    
    ListNode* i = new ListNode(heap.top().first);
    if ((heap.top().second)->next != NULL) heap.push(make_pair(((heap.top().second)->next)->val, (heap.top().second)->next));
    heap.pop();
    ListNode* head = i;
    
    while (heap.size()) {
        i->next = new ListNode(heap.top().first);
        i = i->next;
        
        if ((heap.top().second)->next != NULL) heap.push(make_pair(((heap.top().second)->next)->val, (heap.top().second)->next));
        heap.pop();
    }
    i = NULL;

    return head;
}
