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
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> mp;
        ListNode* cur = head;
        while (cur != nullptr) {
            if (mp.find(cur) != mp.end()) {
                return true;
            }
            mp.insert(cur);
            cur = cur->next;
        }
        return false;
    }
};
