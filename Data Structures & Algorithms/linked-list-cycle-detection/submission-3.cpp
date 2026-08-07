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
        ListNode* odd = head;
        ListNode* even = head;
        while (even && even->next) {
            odd = odd->next;
            even = even->next->next;
            if (odd == even) {
                return true;
            }
        }
        return false;
    }
};
