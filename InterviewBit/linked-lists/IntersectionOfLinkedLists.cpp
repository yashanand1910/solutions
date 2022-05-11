/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int length(ListNode* a) {
    int len = 0;
    while(a != NULL) {
        a = a->next;
        len++;
    }
    return len;
} 
ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
    int diff = length(A) - length(B);
    if (diff >= 0) {
        for(int i = 0; i < diff; i++) A = A->next;
    } else {
        for(int i = 0; i < abs(diff); i++) B = B->next;
    }
    
    while (A != NULL && B != NULL) {
        if (A == B) return A;
        A = A->next;
        B = B->next;
    }
    return NULL;
}
