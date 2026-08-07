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

#include <set>
class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::set<ListNode*> mp;
        ListNode* cur = head;
        while (cur != nullptr) {
            if (mp.contains(cur)) {
                return true;
            }
            mp.insert(cur);
            cur = cur->next;
        }
        return false;
    }
};
