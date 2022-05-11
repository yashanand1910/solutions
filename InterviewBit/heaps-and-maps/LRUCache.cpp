struct DoubleNode {
    DoubleNode* next;
    DoubleNode* prev;
    pair<int, int> val;
    
    DoubleNode(int a, int b): val(make_pair(a, b)), next(NULL), prev(NULL) {}
};

DoubleNode* shiftToFront(DoubleNode* head, DoubleNode* node) {
    (node->prev)->next = node->next;
    if (node->next) (node->next)->prev = node->prev;
    
    node->next = head;
    head->prev = node;
    node->prev = NULL;
    return node;
}

DoubleNode* addToFront(DoubleNode* head, DoubleNode* node) {
    node->next = head;
    head->prev = node;
    return node;
}

int cap, len;
unordered_map<int, DoubleNode*> m;
DoubleNode* head;
DoubleNode* tail;

LRUCache::LRUCache(int capacity) {
    m.clear();
    cap = capacity;
    len = 0;
}

int LRUCache::get(int key) {
    if (m.find(key) != m.end()) {
        if (len != 1 && head != m[key]) {
            if (tail == m[key]) tail = m[key]->prev;
            head = shiftToFront(head, m[key]);
        }
        return (m[key]->val).second;
    } else return -1;
}

void LRUCache::set(int key, int value) {
    if (m.find(key) != m.end()) {
        if (len != 1 && head != m[key]) {
            if (tail == m[key]) tail = m[key]->prev;
            head = shiftToFront(head, m[key]);
        }
        (head->val).second = value;
        (m[key]->val).second = value;
    } else {
        if (len < cap) {
            if (!len) { 
                head = new DoubleNode(key, value);
                tail = head;
            } else head = addToFront(head, new DoubleNode(key, value));
            m.insert({key, head});
            len++;
        } else {
            m.erase((tail->val).first);
            if (len == 1) {
                head = new DoubleNode(key, value);
                tail = head;
            } else {
                head = addToFront(head, new DoubleNode(key, value));
                tail = tail->prev;
                tail->next = NULL;
            }
            m.insert({key, head});
        }
    }
}
