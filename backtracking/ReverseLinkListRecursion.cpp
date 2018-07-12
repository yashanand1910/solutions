/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reverseList(ListNode* A) {
    if (A->next == NULL) {
        return A;
    }
    ListNode* head = reverseList(A->next);
    A->next->next = A;
    A->next = NULL;
    return head;
}
