int length(ListNode* A) {
    int len = 0;
    while(A != NULL) {
        A = A->next;
        len++;
    }
    return len;
}
ListNode* reverse(ListNode* A) {
    ListNode* current = A; ListNode* next; ListNode* prev;
    prev = NULL;
    while(current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
ListNode* Solution::reorderList(ListNode* A) {
    int len = length(A), i = 0;
    ListNode* B = A;
    while(i < (len + 1) / 2 - 1) {
        B = B->next;
        i++;
    }
    ListNode* temp = B;
    B = B->next;
    temp->next = NULL;
    B = reverse(B);
    ListNode* nextA;
    ListNode* nextB;
    ListNode* head = A;

    while(B != NULL) {
        nextA = A->next;
        nextB = B->next;
        A->next = B;
        B->next = nextA;
        A = nextA;
        B = nextB;
    }
    
    return head;
}