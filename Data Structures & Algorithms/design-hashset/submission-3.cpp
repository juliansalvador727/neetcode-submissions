class MyHashSet {
public:
    struct ListNode {
        int val;
        ListNode* next;
        ListNode(int n) : val(n), next(nullptr) {}
    };
    ListNode* head = nullptr;
    MyHashSet() = default;
    
    void add(int key) {
        if (contains(key)) {
            return;
        }
        ListNode* node = new ListNode(key);
        node->next = head;
        head = node;
    }
    
    void remove(int key) {
        ListNode* prev = nullptr;
        ListNode* cur = head;

        while (cur) {
            if (cur->val == key) {
                if (prev) {
                    prev->next = cur->next;
                } else {
                    head = cur->next;
                }

                delete cur;
                return;
            }

            prev = cur;
            cur = cur->next;
        }
    }
    
    bool contains(int key) {
        ListNode* cur = head;
        while (cur) {
            if (cur->val == key) {
                return true;
            }
            cur = cur->next;
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */