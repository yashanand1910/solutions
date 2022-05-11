ListNode* Solution::reverseBetween(ListNode* A, int B, int C) {
    ListNode* current; ListNode* prev; ListNode* next; int curr = 1;
    current = A;
    prev = NULL;
    while(curr != B && current != NULL) {
        prev = current;
        current = current->next;
        curr++;
    }
    ListNode* start = prev;
    ListNode* end = current;
    while(curr != C && end != NULL) {
        end = end->next;
        curr++;
    }
    end = end->next;
    
    prev = end;
    while(current != end) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    if (start == NULL) {
        A = prev;
    } else start->next = prev;
    
    return A;
}
