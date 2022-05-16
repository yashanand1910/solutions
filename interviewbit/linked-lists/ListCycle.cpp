ListNode* Solution::detectCycle(ListNode* A) {
    ListNode* a = A->next; ListNode* b = (A->next)->next;
    int cycleLength;
    while(a != b) {
        a = a->next;
        if(!b->next) return NULL;
        else if(!(b->next)->next) return NULL;
        b = (b->next)->next;
    }

    a = a->next;
    if (a == b) cycleLength = 1;
    else cycleLength = 2;
    while(a->next != b) {
        a = a->next;
        cycleLength++;
    }
    a = b = A; int i = 0;
    while (i < cycleLength) {
        a = a->next;
        i++;
    }
    while (a != b) {
        a = a->next;
        b = b->next;
    }
    
    return a;
}
