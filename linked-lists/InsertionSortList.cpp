ListNode* insertInList(ListNode* A, ListNode* current) {
    ListNode* prev; ListNode* head = A;
    if(current->val <= head->val) {
        current->next = head;
        return current;
    }
    prev = A;
    A = A->next;
    while(A != NULL) {
        if(current->val <= A->val) {
            prev->next = current;
            current->next = A;
            return head;
        }
        prev = A;
        A = A->next;
    }
    prev->next = current;
    current->next = NULL;
    return head;
}
ListNode* Solution::insertionSortList(ListNode* A) {
    ListNode* current = A->next; ListNode* next;
    A->next = NULL;
    while(current != NULL) {
        next = current->next;
        A = insertInList(A, current);
        current = next;
    }
    
    return A;
}
