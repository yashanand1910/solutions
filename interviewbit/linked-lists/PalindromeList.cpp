ListNode* reverse(ListNode* A) {
    ListNode* current; ListNode* next; ListNode* prev;
    current = A;
    prev = NULL;
    while(current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}
string formString(ListNode* A) {
    string output = "";
    while(A != NULL) {
        output += to_string(A->val);
        A = A->next;
    }
    return output;
}
int Solution::lPalin(ListNode* A) {
    string actual, rev;
    actual = formString(A);
    ListNode* B = reverse(A);
    rev = formString(B);

    if (actual == rev) return 1;
    return 0;
}
