RandomListNode* Solution::copyRandomList(RandomListNode* A) {
    unordered_map<RandomListNode*, RandomListNode*> list;
    
    RandomListNode* copyA = new RandomListNode(A->label);
    
    list.insert({A, copyA});
    RandomListNode* temp = copyA;
    while (A != NULL) {
        if (A->next == NULL) {
            temp->next = NULL;
        }
        else if (list.find(A->next) != list.end()) {
            temp->next = list[A->next];
        } else {
            temp->next = new RandomListNode(A->next->label);
            list.insert({A->next, temp->next});
        }
        if (A->random == NULL) {
            temp->random = NULL;
        }
        else if (list.find(A->random) != list.end()) {
            temp->random = list[A->random];
        } else {
            temp->random = new RandomListNode(A->random->label);
            list.insert({A->random, temp->random});
        }
        A = A->next;
        temp = temp->next;
    }
    
    return copyA;
}
