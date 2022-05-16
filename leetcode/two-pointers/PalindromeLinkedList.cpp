/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // O(n) time & O(1) memory solution
    bool isPalindrome(ListNode* head) {
        // First count length of list
        int len = 0;
        ListNode* i = head;
        
        do {
            len++;
            i = i->next;
        } while (i);
        
        if (len == 1) {
            return true;
        }
        
        // Now we find the middle pointer (next to middle in case of odd length)
        ListNode* middle = head;
        
        for(int i = 0; i < len/2; i++) {
            middle = middle->next;
        }
        
        if (len%2 == 1) {
            middle = middle->next;
        }
        
        // We reverse the first half of the linked list
        ListNode* prev = head;
        i = prev->next;
        head->next = NULL;
        
        while (i != middle) {
            ListNode* after = i->next;
            i->next = prev;
            prev = i;
            i = after;
        }
            
        // Compare first and second halves of linked list (should also revert the reversed first half)
        ListNode* start;
        if (len%2 == 1) {
            start = prev->next;
        } else {
            start = prev;
        }
            
        while(middle) {
            if (start->val != middle->val) {
                return false;
            }
            
            middle = middle->next;
            start = start->next;
        }
        
        return true;
    }
};