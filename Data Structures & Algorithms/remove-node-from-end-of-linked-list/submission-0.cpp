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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* cur = head;
        int size = 0;
        while (cur) {
            cur = cur->next;
            size++;
        }
        cur = head;
        ListNode* prev = nullptr;
        int i = size - n;
        while (i--) {
            prev = cur;
            cur = cur->next;
        }
        
        if (prev == nullptr) {
            return head->next;
        }

        prev->next = cur->next;

        return head;
    }
};
